#!/usr/bin/python3
# A script that starts Flask web application

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''It Displays Hello HBNB!'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''It Displays HBNB'''
    return "HBNB"


@app.route("/c/<text>",  strict_slashes=False)
def c_to_text(text):
    '''It display “C ” followed by the value of the text'''
    return 'C ' + text.replace('_', ' ')


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    '''It display python followed by text variables'''
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    '''Starts Flask web application and run on port 5000'''
    app.run(host='0.0.0.0', port=5000)                          
