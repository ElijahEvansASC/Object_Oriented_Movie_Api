from abc import ABC, abstractmethod

#========== Builder Class ==========
class Builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

#========== Media Class ==========
class Media(ABC):
    #Initializes variables
    def __init__ (self, adult: bool, genre_ids: list, id: int, title: str, overview: str, vote_average: float, vote_count: int):
        self.adult = adult
        self.genre_ids = genre_ids
        self.id = id
        self.title = title
        self.overview = overview
        self.vote_average = vote_average
        self.vote_count = vote_count

    def produce_details(self) -> dict:
        pass

#========== MovieBuilder Class ==========
class MovieBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
    #Work here
    def reset(self, adult = False ,genre_ids = [], id = 0, title = "", overview = "", vote_average = 0, vote_count = 0, release_date = "") -> None:
        self._movie = Movie(adult, genre_ids, id, title, overview, vote_average, vote_count, release_date)

    @property
    def movie(self) -> 'Movie':
        movie = self._movie
        self.reset()
        return movie

    def produce_details(self) -> dict:

        return {
            "title": self._movie.title,
            "overview": self._movie.overview,
            "vote_average": self._movie.vote_average
        }

#========== TVShow Builder Class ==========
class TVShowBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self, adult = False ,genre_ids = [], id = 0, title = "", overview = "", vote_average = 0, vote_count = 0, first_air_date = "") -> None:
        self._tvshow = TVShow(adult, genre_ids, id, title, overview, vote_average, vote_count, first_air_date)
        self._tvshow = TVShow()

    @property
    def tvshow(self) -> 'TVShow':
        tvshow = self._tvshow
        self.reset()
        return tvshow

    def produce_details(self) -> dict:

        return {
            "title": self._tvshow.title,
            "overview": self._tvshow.overview,
            "vote_average": self._tvshow.vote_average
        }


#========== Movie Class inheriting from Media Class ==========
class Movie(Media):
    def __init__(self, adult: bool, genre_ids: list, id: int, title: str, overview: str, vote_average: float, vote_count: int, release_date: str):
        #Calls superclass __init__ method to intitalize inherited variables
        super().__init__(adult, genre_ids, id, title, overview, vote_average, vote_count)

        #Initializes unique variable to Movie Class
        self.release_date = release_date

    def produce_details(self) -> dict:
            return {
            "title": self.title,
            "overview": self.overview,
            "vote_average": self.vote_average
        }

#========== TVShow Class inheriting from Media class ==========
class TVShow(Media):
    def __init__(self, adult: bool, genre_ids: list, id: int, title: str, overview: str, vote_average: float, vote_count: int, first_air_date: str):
        #Calls superclass __init__ method to intitalize inherited variables
        super().__init__(adult, genre_ids, id, title, overview, vote_average, vote_count)

        #Initializes unique variable to Movie Class
        self.first_air_date = first_air_date

    def produce_details(self) -> dict:
            return {
            "title": self.title,
            "overview": self.overview,
            "vote_average": self.vote_average
        }    
    

