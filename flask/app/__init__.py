from flask import Flask

app = Flask(__name__)
print("##### Inside init")

from app import views