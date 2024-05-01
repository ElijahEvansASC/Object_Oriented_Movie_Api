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
    return render_template('popular_movie_data.html', popular_movies=popular_movies)

@app.route('/top_rated_movie_data')
def get_top_rated_movie_data():
    process_top_rated_movies_query = ProcessTopRatedMovies()
    context_top_rated_movies_query = Context(process_top_rated_movies_query)
    top_rated_movies = context_top_rated_movies_query.process_query('top_rated_movies')
    return render_template('top_rated_movie_data.html', top_rated_movies=top_rated_movies)

@app.route('/movies')
def get_search_movies():
    search_term = request.args.get('search')

    if not search_term:
        return jsonify({"Error, no search term provided."})

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

#Movie data app routes
#@app.route('/popular_movie_data')
#def get_popular_movie_data():

    #return render_template('popular_movie_data.html', popular_movies = popular_movies)

#@app.route('/top_rated_movie_data')
#def get_top_rated_movie_data():
    #top_rated_movies = ProcessTopRatedMovies.process_top_rated_movies_query()
    #return render_template('top_rated_movie_data.html', top_rated_movies = top_rated_movies)


#Method to run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
    
'''''''''
#TVShows = facade method to get connection string
#Movies = Facade method to get connection string

nextEmployeeId = 4
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist'}), 404
    return jsonify(employee)

def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

def employee_is_valid(employee):
    for key in employee.keys():
        if key != 'name':
            return False
    return True

@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)

    return '', 201, { 'location': f'/employees/{employee["id"]}' }

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    employee.update(updated_employee)

    return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    employees = [e for e in employees if e['id'] != id]
    return jsonify(employee), 200
'''''''''
