from Classes.media import *
import pymongo
import requests

class DBFacade:
    def __init__(self, connection_string, dbname, collectionname):
        self.connection_string = connection_string
        self.dbname = dbname
        self.collectionname = collectionname
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[self.dbname]
        
        #====== Get movie methods ======
    def get_popular_movies(self):
        collection = self.db[self.collectionname]
        query = {}  
        movies = collection.find(query).sort("popularity", pymongo.DESCENDING)
        return list(movies)

    def get_top_rated_movies(self):
        collection = self.db[self.collectionname]
        query = {}
        movies = collection.find(query).sort("vote_average", pymongo.DESCENDING)
        return list(movies)

    def get_movies_by_genre(self, genre_id):
        collection = self.db[self.collectionname]
        query = {}
        movies = collection.find(query).sort("genre_ids", pymongo.DESCENDING)
        return list(movies)
     
    def get_movies_by_search(self, movie_name):
        collection = self.db[self.collectionname]
        query = {"original_title": {"$regex": movie_name, "$options": "i"}}
        movies = collection.find(query)
        return list(movies)
    
