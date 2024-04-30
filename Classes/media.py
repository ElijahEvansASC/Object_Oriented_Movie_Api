from abc import ABC, abstractmethod

#Media Class
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


#Movie class inheriting from Media class
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

#Tv Show class inheriting from Media
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
