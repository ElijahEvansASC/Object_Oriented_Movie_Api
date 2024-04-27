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

    @property
    @abstractmethod
    def Media(self) -> None:
        pass

    @abstractmethod
    def produce_rating(self) -> None:
        pass
    
    @abstractmethod
    def produce_genre_ids(self) -> None:
        pass
    
    @abstractmethod
    def produce_id(self) -> None:
        pass

    @abstractmethod
    def produce_title(self) -> None:
        pass

    @abstractmethod
    def produce_overview(self) -> None:
        pass

    @abstractmethod
    def produce_vote_average(self) -> None:
        pass

    @abstractmethod
    def produce_vote_count(self) -> None:
        pass

#========== MovieBuilder Class ==========
class MovieBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._movie = Movie()

    @property
    def movie(self) -> 'Movie':
        movie = self._movie
        self.reset()
        return movie

    def produce_movie_details(self, movie: 'Movie') -> None:

        movie_details = {
            "title": movie.title,
            "genre_ids": movie.overview,
            "overview": movie.vote_average
        }
        self._movie.append(movie_details)
    
    def produce_extended_movie_details(self, movie: 'Movie') -> None:

        movie_details = {
            "title": movie.title,
            "genre_ids": movie.overview,
            "overview": movie.vote_average
        }

        self._movie.append(movie_details)

#========== TVShow Builder Class ==========
class TVShowBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._tvshow = TVShow()

    @property
    def tvshow(self) -> 'TVShow':
        tvshow = self._tvshow
        self.reset()
        return tvshow

    def produce_tvshow_details(self, tvshow: 'TVShow') -> None:

        tvshow_details = {
            "title": tvshow.title,
            "genre_ids": tvshow.overview,
            "overview": tvshow.vote_average
        }
        self._tvshow.append(tvshow_details)
    
    def produce_extended_tvshow_details(self, tvshow: 'TVShow') -> None:

        tvshow_details = {
            "title": tvshow.title,
            "genre_ids": tvshow.overview,
            "overview": tvshow.vote_average
        }

        self._tvshow.append(tvshow_details)


#========== Movie Class inheriting from Media Class ==========
class Movie(Media):
    def __init__(self, adult: bool, genre_ids: list, id: int, title: str, overview: str, vote_average: float, vote_count: int, release_date: str):
        #Calls superclass __init__ method to intitalize inherited variables
        super().__init__(adult, genre_ids, id, title, overview, vote_average, vote_count)

        #Initializes unique variable to Movie Class
        self.release_date = release_date

    def Media(self) -> None:
        pass

    def produce_rating(self) -> None:
        pass
    
    def produce_genre_ids(self) -> None:
        pass
    
    def produce_id(self) -> None:
        pass

    def produce_title(self) -> None:
        pass

    def produce_overview(self) -> None:
        pass

    def produce_vote_average(self) -> None:
        pass

    def produce_vote_count(self) -> None:
        pass

#========== TVShow Class inheriting from Media class ==========
class TVShow(Media):
    def __init__(self, adult: bool, genre_ids: list, id: int, title: str, overview: str, vote_average: float, vote_count: int, first_air_date: str):
        #Calls superclass __init__ method to intitalize inherited variables
        super().__init__(adult, genre_ids, id, title, overview, vote_average, vote_count)

        #Initializes unique variable to Movie Class
        self.first_air_date = first_air_date
    
    def Media(self) -> None:
        pass

    def produce_rating(self) -> None:
        pass
    
    def produce_genre_ids(self) -> None:
        pass
    
    def produce_id(self) -> None:
        pass

    def produce_title(self) -> None:
        pass

    def produce_overview(self) -> None:
        pass

    def produce_vote_average(self) -> None:
        pass

    def produce_vote_count(self) -> None:
        pass

#========== Director Class ==========
#Optional director class, initializes builder instances so client code can alter type of assembled Media
class Director:
    def __init__(self) -> None:
        self._movie_builder = None
        self._tvshow_builder = None

    @property
    def movie_builder(self) -> MovieBuilder:
        return self._movie_builder
    
    @property
    def tvshow_builder(self) -> TVShowBuilder:
        return self._movie_builder

    @movie_builder.setter
    def movie_builder(self, movie_builder: MovieBuilder) -> None:
        self._movie_builder = movie_builder
    
    @tvshow_builder.setter
    def tvshow_builder(self, tvshow_builder: TVShowBuilder) -> None:
        self._tvshow_builder = tvshow_builder

    #Basic movie listing(title, genre_ids key value, overview)
    def build_basic_movie_listing(self) -> None:
        self.movie_builder.produce_movie_details()
    
    #Extended movie listing (all properties and values)
    def build_basic_tvshow_listing(self) -> None:
        self.tvshow_builder.produce_tvshow_details()

    def build_extended_movie_listing(self) -> None:
        self.movie_builder.produce_movie_details()
        self.movie_builder.produce_extended_movie_details()
    
    def build_extended_tvshow_listing(self) -> None:
        self.tvshow_builder.produce_movie_details()
        self.tvshow_builder.produce_extended_movie_details()