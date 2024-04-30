from __future__ import annotations
from abc import ABC, abstractmethod
from Classes.create_and_query_endpoints import Facade
from Tools import *
import json

facade = Facade(api_key='e41e13373c979e318ae4ca2804ec7e2a', base_url = 'https://api.themoviedb.org/3')

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
        tmdb_response_text = facade.get_popular_movies()
        tmdb_response = json.loads(tmdb_response_text)
        return Tools.create_movie_listing(tmdb_response)


    #Stub methods had to be implemented in each class to fulfill inheriting from the Strategy class.
    def process_top_rated_movies_query(self):
        pass
    def process_search_movies_query(self):
        pass


class ProcessTopRatedMovies(Strategy):
    def process_top_rated_movies_query(self):
        tmdb_response_text = facade.get_top_rated_movies()
        tmdb_response = json.loads(tmdb_response_text)
        return Tools.create_movie_listing(tmdb_response)

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