from flask import Flask
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://mongo:27017/myusers"
mongo = PyMongo(app)

from app import views