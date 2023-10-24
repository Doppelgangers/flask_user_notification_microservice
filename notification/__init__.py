from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

#configs
app.config["SECRET_KEY"] = "48d6ffc0df5699e2954bc5628ccb00c6b3b5d22"
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

#setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from notification import routes
