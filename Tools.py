from Classes.media import Movie
from pymongo import MongoClient

class Tools:
    @staticmethod
    def create_movie_listing(json_object):
        results = json_object.get("results", [])
        movie_list = []
        for movie_data in results:
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
    