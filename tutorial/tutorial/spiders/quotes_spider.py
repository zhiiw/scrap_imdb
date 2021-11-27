import re

import pymongo
import scrapy


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
                urls.append('https://www.themoviedb.org/tv/' + row['tmdbId'])
                print(row['movieId'], row['imdbId'])

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    ## response.css('li.card p a').getall()
    ## response.css('div.overview p').get()

    def parse(self, response):
        page = response.url.split("/")[-1]
        name = response.css('h2 a').get()

        actor_list = ""
        str = re.search('[0-9]+', page).group()
        overview = response.css('div.overview p').get()
        for actor in response.css('li.card p a'):
            actor_list+=actor.get()
        id = int(str)
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient["tmdb"]
        mycol = mydb["video"]
        mylist = {"movieId": id, "name": name, "overview": overview, "actor_list": actor_list}
        x = mycol.insert_one(mylist)
        print(x.inserted_id)
        # print list of the _id values of the inserted documents:
