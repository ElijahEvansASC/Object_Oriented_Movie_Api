from Tools import *
from Classes.process_queries import *
from flask import Flask, render_template


#To Run the Server:
# 1.) Start debugging app.py
# 2.) Navigate to http://127.0.0.1:5000 for the base URL

#Flask application
app = Flask(__name__)

#Base URL view app route
@app.route('/')
def hello():
    return 'Hello, World!'
    
#Movie data app routes
@app.route('/popular_movie_data')
def get_popular_movie_data():
    popular_movies = ProcessPopularMovies.process_popular_movies_query()
    return render_template('popular_movie_data.html', popular_movies = popular_movies)

@app.route('/top_rated_movie_data')
def get_top_rated_movie_data():
    top_rated_movies = ProcessTopRatedMovies.process_top_rated_movies_query()
    return render_template('top_rated_movie_data.html', top_rated_movies = top_rated_movies)


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
