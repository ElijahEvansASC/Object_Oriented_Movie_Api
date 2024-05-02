from flask import Flask, render_template, request, jsonify
from Classes.process_queries import *
from Tools import *  # Importing the entire Tools module

# Flask application
app = Flask(__name__)

# Base URL view app route
@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/popular_movie_data')
def get_popular_movie_data():
    process_popular_movies_query = ProcessPopularMovies()
    context_popular_movies_query = Context(process_popular_movies_query)
    popular_movies = context_popular_movies_query.process_query('popular_movies')
    built_popular_movies = Tools.create_movie_listing(popular_movies)
    return render_template('popular_movie_data.html', built_popular_movies = built_popular_movies)

@app.route('/top_rated_movie_data')
def get_top_rated_movie_data():
    process_top_rated_movies_query = ProcessTopRatedMovies()
    context_top_rated_movies_query = Context(process_top_rated_movies_query)
    top_rated_movies = context_top_rated_movies_query.process_query('top_rated_movies')
    built_top_rated_movies = Tools.create_movie_listing(top_rated_movies)
    return render_template('top_rated_movie_data.html', built_top_rated_movies = built_top_rated_movies)


#Not working
@app.route('/movies')
def get_search_movies():
    search_term = request.args.get('search')
    search_results = []
    process_search_movies_query = ProcessSearchMovies()
    context_search_movies_query = Context(process_search_movies_query)
    search_movies = context_search_movies_query.process_query('search_movies')
    for movie in search_movies:
       if search_term.lower() in movie['title'].lower():
            search_results.append(movie)
    return render_template('search_movie_data.html', search_results = search_results)

# Method to run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

