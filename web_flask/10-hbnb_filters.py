#!/usr/bin/python3
"""Script that starts Flask web application"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''It displays template with states'''
    route = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(route, states=states, amenities=amenities)


@app.teardown_appcontext
def app_teardown(arg=None):
    '''This clean-up the session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
