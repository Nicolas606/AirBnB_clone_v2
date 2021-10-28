#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask, render_template
import models
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def removeSQLAlchemySession(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def stateList():
    """display a HTML page: (inside the tag BODY)"""
    states_all = storage.all(State).values()
    states = sorted(states_all, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
