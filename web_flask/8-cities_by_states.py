#!/usr/bin/python3
"""Script that starts web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    '''It displays the template with states'''
    route = '8-cities_by_states.html'
    states = storage.all(State)
    # This will sort State object alphabetically by name
    return render_template(route, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    ''' This clean-up session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
