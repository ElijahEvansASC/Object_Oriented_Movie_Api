from flask import Flask

#To Run the Server:
# 1.) Start debugging app.py
# 2.) Navigate to http://127.0.0.1:5000

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)