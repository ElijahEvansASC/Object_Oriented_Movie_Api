from __future__ import annotations
from abc import ABC, abstractmethod
from pymongo import MongoClient
from Tools import *

#Context class, holds all query process functions
class Context():

    def __init__(self, strategy: Strategy) -> None:
 
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
  
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
 
        self._strategy = strategy

    def process_query(self, process: str):
        if process == 'popular_movies':
            return self._strategy.process_popular_movies_query()
        elif process == 'top_rated_movies':
            return self._strategy.process_top_rated_movies_query()
        elif process == 'search_movies':
            return self._strategy.process_search_movies_query()
        elif process == 'popular_tvshows':
            return self._strategy.process_popular_tvshows_query()
        elif process == 'top_rated_tvshows':
            return self._strategy.process_top_rated_tvshows_query()
        elif process == 'search_tvshows':
            return self._strategy.process_search_tvshows_query()
        


#Strategy pattern methods, each function declares an abstract method that is passed to all strategies for media data.
class Strategy(ABC):

    @abstractmethod
    def process_popular_movies_query(self):
        pass

    @abstractmethod
    def process_top_rated_movies_query(self):
        pass

    @abstractmethod
    def process_search_movies_query(self):
        pass

    @abstractmethod
    def process_popular_tvshows_query(self):
        pass

    @abstractmethod
    def process_top_rated_tvshows_query(self):
        pass

    @abstractmethod
    def process_search_tvshows_query(self):
        pass


class ProcessPopularMovies(Strategy):
    def process_popular_movies_query(self):
        # Connect to MongoDB and fetch popular movies
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        #finds movies based on popularity, sorts highest popularity to be printed first
        popular_movies = list(db.Movies.find({"popularity": {"$gt": 0}}).sort("popularity", -1))
        return popular_movies


    #Stub methods implemented as a requirement of inheriting from the Strategy class
    def process_top_rated_movies_query(self):
        pass
    def process_search_movies_query(self):
        pass
    
    def process_popular_tvshows_query(self):
        pass

    def process_top_rated_tvshows_query(self):
        pass

    def process_search_tvshows_query(self):
        pass


class ProcessTopRatedMovies(Strategy):
    def process_top_rated_movies_query(self):
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        #finds movies based on rating, sorts highest rating to be printed first
        top_rated_movies = list(db.Movies.find({"vote_average": {"$gt": 7.5}}).sort("vote_average", -1))
        return top_rated_movies

    #Unused functions are passed
    def process_popular_movies_query(self):
        pass
    def process_search_movies_query(self):
        pass

    def process_popular_tvshows_query(self):
        pass

    def process_top_rated_tvshows_query(self):
        pass

    def process_search_tvshows_query(self):
        pass

    
class ProcessSearchMovies(Strategy):
    def process_search_movies_query(self):
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        #Returns all movies, sorts them Z-A
        search_movies:list = list(db.Movies.find().sort('title', -1))
        return search_movies

    def process_popular_movies_query(self):
        pass
    def process_top_rated_movies_query(self):
        pass

    def process_popular_tvshows_query(self):
        pass

    def process_top_rated_tvshows_query(self):
        pass

    def process_search_tvshows_query(self):
        pass

#TvShow classes and functions have the same logic as movies, with a different data table of TvShows
class ProcessPopularTvShows(Strategy):
     def process_popular_tvshows_query(self):
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        popular_tvshows = list(db.TvShows.find({"popularity": {"$gt": 0}}).sort("popularity", -1))
        return popular_tvshows
     
     def process_popular_movies_query(self):
         pass
     
     def process_top_rated_movies_query(self):
         pass
     
     def process_search_movies_query(self):
        pass

     def process_popular_tvshows_query(self):
         pass

     def process_top_rated_tvshows_query(self):
         pass

     def process_search_tvshows_query(self):
         pass
     
class ProcessTopRatedTvShows(Strategy):
     def process_top_rated_tvshows_query(self):
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        top_rated_tvshows = list(db.TvShows.find({"vote_average": {"$gt": 7.5}}).sort("vote_average", -1))
        return top_rated_tvshows
     
     def process_popular_movies_query(self):
         pass
     
     def process_top_rated_movies_query(self):
         pass
     
     def process_search_movies_query(self):
        pass

     def process_popular_tvshows_query(self):
         pass

     def process_search_tvshows_query(self):
         pass
     
class ProcessSearchTvShows(Strategy):
    def process_search_movies_query(self):
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        search_tvshows:list = list(db.TvShows.find().sort('title', -1))
        return search_tvshows

    def process_popular_movies_query(self):
        pass
    def process_top_rated_movies_query(self):
        pass

    def process_search_movies_query(self):
        pass

    def process_popular_tvshows_query(self):
        pass

    def process_top_rated_tvshows_query(self):
        pass

