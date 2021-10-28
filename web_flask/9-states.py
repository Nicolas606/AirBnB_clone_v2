#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def removeSQLAlchemySession(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page: (inside the tag BODY)"""
    all_states = storage.all(State)
    return render_template("9-states.html",
                           states=all_states, page="state")


@app.route("/states/<id>", strict_slashes=False)
def state_cities(id):
    """display a HTML page: (inside the tag BODY)"""
    all_states = storage.all(State)
    key = "State." + id
    if key in all_states:
        return render_template("9-states.html",
                               page="state_cities", state=all_states[key])
    else:
        return render_template("9-states.html", page="Not found!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
