from Classes.media import *
from Classes.create_and_query_endpoints import *
import json

facade = Facade(api_key='e41e13373c979e318ae4ca2804ec7e2a', base_url = 'https://api.themoviedb.org/3')

class Tools:
     def create_movie_listing(json_object):
        results = json_object.get("results", [])
        movie_list = []
        for movie_data in results:  # Iterate over each movie dictionary
        # Access individual keys and values
            adult = movie_data.get('adult')
            genre_ids = movie_data.get('genre_ids')
            id = movie_data.get('id')
            title = movie_data.get('title')
            overview = movie_data.get('overview')
            vote_average = movie_data.get('vote_average')
            vote_count = movie_data.get('vote_count')
            release_date = movie_data.get('release_date')
            movie = Movie(adult, genre_ids, id, title, overview, vote_average, vote_count, release_date)
            movie_list.append(movie)
        return movie_list

     def process_popular_movie_query():
        tmdb_response_text = facade.get_popular_movies()
        tmdb_response = json.loads(tmdb_response_text)
        return Tools.create_movie_listing(tmdb_response)
     
     def process_top_rated_movie_query():
        tmdb_response_text = facade.get_top_rated_movies()
        tmdb_response = json.loads(tmdb_response_text)
        return Tools.create_movie_listing(tmdb_response)
                            