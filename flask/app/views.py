
from app import app, mongo
from flask import request, jsonify
import os

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")
    port = os.getenv("FLASK_PORT")
    if app_name:
        response = {}
        response['port'] = port
        response['user_key'] = None
        if request.args and ('user_id' in request.args):
            user_id = request.args.get('user_id')
            user_key_cursor = mongo.db.data.find({"user_id": user_id})
            for item in user_key_cursor:
                response['user_key'] = item['user_key']
            # return jsonify(response)
        return jsonify(response)
    return "Flask: Hello"