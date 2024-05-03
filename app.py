from flask import Flask, render_template, request, jsonify
from Classes.process_queries import *
from Tools import *  # Importing the entire Tools module

# Flask application
app = Flask(__name__)

# Base URL view app route
@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/popular_movie_data') #Declares an app route as the url extension /popular_movie_data
def get_popular_movie_data():
    process_popular_movies_query = ProcessPopularMovies()
    context_popular_movies_query = Context(process_popular_movies_query)
    popular_movies = context_popular_movies_query.process_query('popular_movies')
    built_popular_movies = Tools.create_movie_listing(popular_movies)
    return render_template('popular_movie_data.html', built_popular_movies = built_popular_movies) #renders the corresponding html template and passes in built_popular_movies to the jinja statements 

@app.route('/top_rated_movie_data')
def get_top_rated_movie_data():
    process_top_rated_movies_query = ProcessTopRatedMovies()
    context_top_rated_movies_query = Context(process_top_rated_movies_query)
    top_rated_movies = context_top_rated_movies_query.process_query('top_rated_movies')
    built_top_rated_movies = Tools.create_movie_listing(top_rated_movies)
    return render_template('top_rated_movie_data.html', built_top_rated_movies = built_top_rated_movies)


#App route for searching movies
# search_results array is initialized, for every movie in search_movies whose string value matches the search term in
@app.route('/movies')
def get_search_movies():
    search_term = request.args.get('search')
    search_results = []
    process_search_movies_query = ProcessSearchMovies()
    context_search_movies_query = Context(process_search_movies_query)
    search_movies = context_search_movies_query.process_query('search_movies')
    for movie in search_movies:
       if search_term.lower() in movie['title'].lower(): #If the search_term in lowercase matches the movie title in lowercase, it is appended to the initialized search_results list
            search_results.append(movie)
    return render_template('search_movie_data.html', search_results = search_results)

@app.route('/popular_tvshow_data')
def get_popular_tvshow_data():
    process_popular_tvshows_query = ProcessPopularTvShows()
    context_popular_tvshows_query = Context(process_popular_tvshows_query)
    popular_tvshows = context_popular_tvshows_query.process_query('popular_tvshows')
    built_popular_tvshows = Tools.create_tvshow_listing(popular_tvshows)
    return render_template('popular_tvshows_data.html', built_popular_tvshows = built_popular_tvshows)


# Method to run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

