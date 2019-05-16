from flask import Flask
import os
from flask_pymongo import PyMongo

app = Flask(__name__)
username = os.getenv("MONGO_USER")
pwd = os.getenv("MONGO_PASS")
app.config['MONGO_URI'] = "mongodb://{}:{}@mongo:27017/myusers".format(username, pwd).replace('"', '')
mongo = PyMongo(app)

from app import views