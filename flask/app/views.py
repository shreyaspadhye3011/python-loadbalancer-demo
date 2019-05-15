
from app import app, mongo
from flask import request
import os

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")
    port = os.getenv("FLASK_PORT")
    if app_name:
        if request.args and ('user_id' in request.args):
            user_id = request.args.get('user_id')
            # TODO: plug in code to fetch key value from mongodb
            test_user = mongo.db.data.find({"user_id": 1})
            print("*********")
            print(type(test_user))
            return "user_id: {}, port: {}".format(user_id, port)
        return "Currently Serving: {} from port: {}".format(app_name, port)
    return "Flask: Hello"