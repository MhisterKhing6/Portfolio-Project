#!/usr/bin/python3
from flask import Flask, Blueprint, session
session_managment = session
from api import app
run_app = Flask(__name__)
run_app.secret_key = "9%8%7521kofikofi"

run_app.register_blueprint(app)
if __name__ == "__main__":
    run_app.run(host="0.0.0.0", port='5000', debug=True)
