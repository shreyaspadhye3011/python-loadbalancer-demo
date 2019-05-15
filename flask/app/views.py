
from app import app
from flask import request
import os

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        if request.args:
            
            return "Logic to get keys under development"
        return "Docker App Currently Serving: {}".format(app_name)

    return "Flask: Hello"