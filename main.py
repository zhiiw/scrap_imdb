# import re
#
# import numpy as np
# from sklearn.model_selection import train_test_split
# import pandas as pd
# import pandas as pd
# import numpy as np
# import pymongo
# """
# df = pd.read_csv('ratings.csv')
# df['split'] = np.random.randn(df.shape[0], 1)
#
# msk = np.random.rand(len(df)) <= 0.8
#
# train = df[msk]
# print(train.size)
#
# test = df[~msk]
# print(test.size)
# print(test)
#
# train.to_csv('ratings_train.csv',index=False)
# test.to_csv('ratings_test.csv',index=False)
# """
# '''
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient["mydatabase"]
# dblist = myclient.list_database_names()
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)
#
# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)
# print(mydb.list_collection_names())
#
# mycol = mydb["customers"]
# if "mydatabase" in dblist:
#   print("The database exists.")
#
# print(myclient.list_database_names())
# '''
# # headline ="114514-rgads"
# # str=re.search('[0-9]+', headline).group()
# # print(str)
# #
# #
# #
# #
# # from featuretools import primitives
# # from sklearn.datasets import load_iris
# # import pandas as pd
# # import featuretools as ft
# # from sklearn.datasets._base import load_csv_data
# #
# # from featuretools.selection import (
# #     remove_highly_correlated_features,
# #     remove_highly_null_features,
# #     remove_single_value_features,
# # )
# #
# # # Load data and put into dataframe
# #
# # df = pd.read_csv("Train_data.csv", index_col=0)
# #
# # # Make an entityset and add the entity
# # es = ft.EntitySet(id='detector')
# # es.add_dataframe(dataframe_name='data', dataframe=df,
# #                  make_index=True, index='index')
# #
# # # Run deep feature synthesis with transformation primitives
# # feature_matrix, feature_defs = ft.dfs(entityset=es, target_dataframe_name='data',
# #                                       trans_primitives=['add_numeric', 'multiply_numeric'])
# #
# # new_fm, new_features = remove_single_value_features(feature_matrix, features=feature_defs)
# #
# # new1_fm, new1_features = remove_highly_correlated_features(new_fm, features=new_features,
# #                                                            pct_corr_threshold=.5)
# #
# # print(new1_fm)
# # new1_fm.to_csv("e.csv")
# # new1_fm.head()
#
# import pandas as pd
# import numpy as np
# data = pd.read_csv('ratings.csv')
# data['userId'] = data['userId'].astype('str')
# data['movieId'] = data['movieId'].astype('str')
# users = data['userId'].unique() #list of all users
# movies = data['movieId'].unique() #list of all movies
# print("Number of users", len(users))
# print("Number of movies", len(movies))
# print(data.head())
import re

str= '35-sally-field'

actor_name = re.sub(r'\D', "", str)
print(actor_name)