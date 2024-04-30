from __future__ import annotations
from abc import ABC, abstractmethod
from Tools import *

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


#Strategy pattern methods, each function declares an abstract method.
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


class ProcessPopularMovies(Strategy):
    def process_popular_movies_query(self):
        # Connect to MongoDB and fetch popular movies
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        popular_movies = list(db.Movies.find({"popularity": {"$gt": 0}}))
        return popular_movies


    #Stub methods had to be implemented in each class to fulfill inheriting from the Strategy class.
    def process_top_rated_movies_query(self):
        pass
    def process_search_movies_query(self):
        pass


class ProcessTopRatedMovies(Strategy):
    def process_top_rated_movies_query(self):
        # Connect to MongoDB and fetch top rated movies
        client = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
        db = client.MovieDatabase
        top_rated_movies = list(db.Movies.find({"vote_average": {"$gt": 7.5}}))
        return top_rated_movies

    def process_popular_movies_query(self):
        pass
    def process_search_movies_query(self):
        pass

    
class ProcessSearchMovies(Strategy):
    def process_search_movies_query(self):
        #Code here
        print("Awaiting implementation.")

    def process_popular_movies_query(self):
        pass
    def process_top_rated_movies_query(self):
        pass