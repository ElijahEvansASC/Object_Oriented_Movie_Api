from __future__ import annotations
from abc import ABC, abstractmethod



class Context():

    def __init__(self, strategy: Strategy) -> None:
 
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
  
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
 
        self._strategy = strategy

    def process_query(self, string: str, process: str) -> str:
        if process == 'popular_movies':
            return self._strategy.process_popular_movies_query(string)
        elif process == 'top_rated_movies':
            return self._strategy.process_top_rated_movies_query(string)
        elif process == 'search_movies':
            return self._strategy.process_search_movies_query(string)


#Strategy pattern methods, each function declares an abstract method for calculating hash functions supported by the hashlib library.
class Strategy(ABC):

    @abstractmethod
    def process_popular_movies_query(self, string: str) -> str:
        pass

    @abstractmethod
    def process_top_rated_movies_query(self, string: str) -> str:
        pass

    @abstractmethod
    def process_search_movies_query(self, string: str) -> str:
        pass


class ProcessPopularMovies(Strategy):
    def process_popular_movies_query(self, string: str) -> str:
        #Code here


    #Stub methods had to be implemented in each class to fulfill inheriting from the Strategy class.
    def process_top_rated_movies_query(self, string: str) -> str:
        pass
    def process_search_movies_query(self, string: str) -> str:
        pass


class ProcessTopRatedMovies(Strategy):
    def process_top_rated_movies_query(self, string: str) -> str:
        #Code here

    def process_popular_movies_query(self, string: str) -> str:
        pass
    def process_search_movies_query(self, string: str) -> str:
        pass

    
class ProcessSearchMovies(Strategy):
    def process_search_movies_query(self, string: str) -> str:
        #Code here

    def process_popular_movies_query(self, string: str) -> str:
        pass
    def process_top_rated_movies_query(self, string: str) -> str:
        pass