#!/usr/bin/python3
import sys
import os
from flask import Flask
from flask import render_template

module_dir = os.path.abspath("/root/holbertonschool-AirBnB_clone_v2/")

if module_dir not in sys.path:
    sys.path.append(module_dir)

from models import storage

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
