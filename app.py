from flask import Flask
from routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv() #will load the dotenv file


def create_app():
    app = Flask(__name__)
    client =MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()
    app.register_blueprint(pages)
    return app