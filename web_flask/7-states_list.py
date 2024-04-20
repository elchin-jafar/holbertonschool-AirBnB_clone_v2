#!/usr/bin/python3
"""display states_list from db"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    result = sorted(obj, key=lambda x: x.name)
    return render_template("7-states_list.html", states=result)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
