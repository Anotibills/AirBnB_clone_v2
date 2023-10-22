#!/usr/bin/python3
# A script that starts Flask web application

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
    '''It Displays Hello HBNB!'''
def hello_hbhb():
    return "Hello HBNB!"

if __name__ == '__main__':
    '''Starts Flask web application and run on port 5000'''
    app.run(host='0.0.0.0', port=5000)
