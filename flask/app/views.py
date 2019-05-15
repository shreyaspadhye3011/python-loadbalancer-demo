
from app import app
from flask import request
import os

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        if request.args and ('user_id' in request.args):
            user_id = request.args.get('user_id')
            return user_id
            # return "Logic to get keys under development"
        return "Currently Serving: {}".format(app_name)
    return "Flask: Hello"