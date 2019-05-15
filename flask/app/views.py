
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
            user_key = None
            user_key_cursor = mongo.db.data.find({"user_id": user_id})
            print("######", user_key_cursor.count())
            # TODO: plug in code to test whether anything was found
            for item in user_key_cursor:
                user_key = item['user_key']
            return "user_key: {}, port: {}".format(user_key, port)
        return "Currently Serving: {} from port: {}".format(app_name, port)
    return "Flask: Hello"