import re
import redis
import pymongo
import scrapy

redis_conn = redis.Redis(host='localhost', port=6379, db=0)


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):

        import csv
        array = []
        urls = []
        count = 0;
        with open('links.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                array.append(row['imdbId'])
                urls.append('https://www.themoviedb.org/movie/' + row['tmdbId'])

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        score = response.css('div.user_score_chart').re(r'data-percent="\d+')
        score = int(score[0].replace('data-percent="', ''))
        tags = response.css('div.facts span.genres a::text').getall()
        runtime = response.css('div.facts span.runtime::text').getall()
        other_info = response.css('section.facts p::text ').getall()
        page = response.url.split("/")[-1]
        name = response.css('h2 a').get()
        director_index = response.css('ol.people li p.character::text').getall()
        director_use = ""
        for i in range(len(director_index)):
            if director_index[i] == 'Director':
                director = response.css('ol.people li a').getall()[i]
                ee = director.replace('<a href="/person/', '')
                director_id = re.sub(r'-.*$', "", ee)
                redis_conn.sadd("2",director_id)
                director_name = re.sub(r'^.*">', "", director)
                director_name = re.sub(r'</a>$', "", director_name)
                director_use += director_id + " " + director_name + "\n"
                break
        actor_list = ""
        str = re.search('[0-9]+', page).group()
        id = int(str)

        overview = response.css('div.overview p::text').get()
        for actor in response.css('li.card p a'):
            str = actor.get()
            ee = str.replace('<a href="/person/', '')
            actor_id = re.sub(r'-.*$', "", ee)
            redis_conn.sadd("2",actor_id)
            actor_name = re.sub(r'^.*">', "", str)
            actor_name = re.sub(r'</a>$', "", actor_name)
            actor_list += actor_id + " " + actor_name + "\n"

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient["tmdb"]
        mycol = mydb["video"]
        mylist = {"movieId": id, "name": name, "overview": overview, "actor_list": actor_list, "score": score,
                  "director": director_use, "tags": tags, "runtime": runtime, "other_info": other_info}
        x = mycol.insert_one(mylist)

        # print list of the _id values of the inserted documents:
