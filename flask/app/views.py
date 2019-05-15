
from app import app
import os

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return "Docker App Currently Serving: {}".format(app_name)

    return "Flask: Hello"