from Classes.media import *

class Tools:
    #Static method that takes the json_data from a table as a parameter
    @staticmethod
    def create_movie_listing(json_object):
        movie_list = [] #initializes empty list of movies
        movie_builder = MovieBuilder() #Instantiates MovieBuilder class in the variable movie_builder
        for movie_data in json_object: #Iterates through every movie's data in the json object with a for loop
            movie_builder.reset(
                adult = movie_data.get('adult'),
                genre_ids = movie_data.get('genre_ids'),
                id = movie_data.get('id'),
                title = movie_data.get('title'),
                overview = movie_data.get('overview'),
                vote_average = movie_data.get('vote_average'),
                vote_count = movie_data.get('vote_count'),
                popularity = movie_data.get('popularity'),
                release_date = movie_data.get('release_date')
            )
            movie = movie_builder.movie
            movie_list.append(movie) #Appends the movie to the initialized empty list
        return movie_list #Returns the movie list
    
    #This static method has the same logic as create_movie_listing(), except for tvshow data
    @staticmethod
    def create_tvshow_listing(json_object):
        tvshow_list = []
        tvshow_builder = TVShowBuilder()
        for tvshow_data in json_object:
            tvshow_builder.reset(
                adult = tvshow_data.get('adult'),
                genre_ids = tvshow_data.get('genre_ids'),
                id = tvshow_data.get('id'),
                title = tvshow_data.get('title'),
                overview = tvshow_data.get('overview'),
                vote_average = tvshow_data.get('vote_average'),
                vote_count = tvshow_data.get('vote_count'),
                popularity = tvshow_data.get('popularity'),
                first_air_date = tvshow_data.get('first_air_date')
            )
            tvshow = tvshow_builder.tvshow
            tvshow_list.append(tvshow)
        return tvshow_list
    




    