from Classes import gvars
from flask import Flask, jsonify, request, json

#To Run the Server:
# 1.) Start debugging app.py
# 2.) Navigate to http://127.0.0.1:5000 for the base URL

app = Flask(__name__)

#Declaring gvars class to be passed around the program
g_vars = gvars.GVars() 
#Declaring database connection string using pymongo
database = g_vars.connect_to_mongo_db(g_vars.db_name, g_vars.connection_string)

#Base URL view app route
@app.route('/')
def hello():
    return 'Hello, World!'

#Defines and stores data from tables in database

#TVShows = facade method to get connection string
#Movies = Facade method to get connection string
employees = [
    { 'id': 1, 'name': 'Ashley' },
    { 'id': 2, 'name': 'Kate' },
    { 'id': 3, 'name': 'Joe' }
]


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

#Method to run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)