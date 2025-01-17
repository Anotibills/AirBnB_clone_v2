#!/usr/bin/python3
"""Script that start web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''It displays list of all states'''
    route = '7-states_list.html'
    states = storage.all(State)
    # This will sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(route, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    '''This clean-up sessions'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
