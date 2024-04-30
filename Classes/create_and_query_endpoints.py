from Classes.media import *
import requests

#====== Subroutine One: RunMediaQuery ======
class RunMediaQuery:
    @staticmethod
    def run_media_query(url):
          headers = {"accept": "application/json"}
          response = requests.get(url, headers=headers)
          return response.text

#====== Subroutine Two: CreateQueryEndpoint ====== 
class CreateQueryEndpoint:
    def __init__(self, api_key, base_url):
        self.api_key = api_key #e41e13373c979e318ae4ca2804ec7e2a
        self.base_url = base_url 
  #====== Get movie url methods ======
    def get_movie_by_genre_url(self, genre_id):
        return f"{self.base_url}/discover/movie?api_key={self.api_key}&with_genres={genre_id}"

    def get_movie_by_popular_url(self):
        return f"{self.base_url}/movie/top_rated?api_key={self.api_key}"
    
    def get_movie_by_top_rated_url(self):
        return f"{self.base_url}/movie/popular?api_key={self.api_key}"
    
    def get_movie_by_search_url(self, search_term):
         return f"{self.base_url}/movie/popular?api_key={self.api_key}&query={search_term}"
  #====== Get tvshow url methods ======
    def get_tvshows_by_genre_url(self, genre_id):
        return f"{self.base_url}/discover/tv?api_key={self.api_key}&with_genres={genre_id}"
    
    def get_tvshows_by_popular_url(self):
        return f"{self.base_url}/tv/top_rated?api_key={self.api_key}"
    
    def get_tvshows_by_top_rated_url(self):
        return f"{self.base_url}/tv/popular?api_key={self.api_key}"
    
    def get_tvshows_by_search_url(self, search_term):
         return f"{self.base_url}/tv/popular?api_key={self.api_key}&query={search_term}"
    
#====== Facade Class ======
class Facade:
    def __init__(self, api_key, base_url) -> None:
        self.query_endpoint = CreateQueryEndpoint(api_key, base_url)
        self.media_query = RunMediaQuery()

    #This function gets the resulting json object and builds individual objects for each movie in that listing.
    #This function supports only one page of results, which should be fine for our search methods.
    #def create_movie_listing(json_object):
        #results = json_object.get("results", [])
        #for movie_data in results:  # Iterate over each movie dictionary
            # Access individual keys and values
            #adult = movie_data.get('adult')
            #genre_ids = movie_data.get('genre_ids')
            #movie_id = movie_data.get('id')
            #title = movie_data.get('title')
            #overview = movie_data.get('overview')
            #vote_average = movie_data.get('vote_average')
            #vote_count = movie_data.get('vote_count')
            #release_date = movie_data.get('release_date')
            # Create Movie object with individual attributes
            #movie = Movie(adult, genre_ids, movie_id, title, overview, vote_average, vote_count, release_date)

    
    #def create_tvshow_listing(json_object):
        #results = json_object.get("results", [])
        #for tv_data in results:  # Iterate over each movie dictionary
            # Access individual keys and values
            #adult = tv_data.get('adult')
            #genre_ids = tv_data.get('genre_ids')
            #movie_id = tv_data.get('id')
            #title = tv_data.get('title')
            #overview = tv_data.get('overview')
            #vote_average = tv_data.get('vote_average')
            #vote_count = tv_data.get('vote_count')
            #first_air_date = tv_data.get('first_air_date')
            # Create TVShow object with individual attributes
            #tvshow = TVShow(adult, genre_ids, movie_id, title, overview, vote_average, vote_count, first_air_date)


  #====== Get movie methods ======
    def get_popular_movies(self):
        url= self.query_endpoint.get_movie_by_popular_url()
        return self.media_query.run_media_query(url)

    def get_top_rated_movies(self):
        url= self.query_endpoint.get_movie_by_top_rated_url()
        return self.media_query.run_media_query(url)

    def get_movies_by_genre(self, genre_id):
         url= self.query_endpoint.get_movie_by_genre_url(genre_id)
         return self.media_query.run_media_query(url)
     
    def get_movies_by_search(self, search_term):
         url = self.query_endpoint.get_movie_by_search_url(search_term)
         return self.media_query.run_media_query(url)
  #====== Get tvshow methods ======
    def get_popular_tvshows(self):
        url= self.query_endpoint.get_tvshows_by_popular_url()
        return self.media_query.run_media_query(url)

    def get_top_rated_tvshows(self):
        url= self.query_endpoint.get_tvshows_by_top_rated_url()
        return self.media_query.run_media_query(url)

    def get_tvshows_by_genre(self, genre_id):
         url= self.query_endpoint.get_tvshows_by_genre_url(genre_id)
         return self.media_query.run_media_query(url)
     
    def get_tvshows_by_search(self, search_term):
         url = self.query_endpoint.get_tvshows_by_search_url(search_term)
         return self.media_query.run_media_query(url)
  


#Example Usage:
#Note that some functions require a parameter that will have to be declared through user input decisions.
#For TVShows, replace "movies" with "tvshows" in function names.

#if __name__ == "__main__":
#     api_key = "e41e13373c979e318ae4ca2804ec7e2a"
#     base_url = "https://api.themoviedb.org/3"
#
#     facade = Facade(api_key, base_url)
#

#     facade.get_popular_movies()
#
#     facade.get_top_rated_movies()
#     
#     genre_id = 28
#     facade.get_movies_by_genre(genre_id)
#
#     search_term = "lord%20of%20the%20%rings"
#     facade.get_movies_by_search(search_term)
