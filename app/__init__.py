from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from environs import Env
from app import views

env = Env()
env.read_env()

db = SQLAlchemy()
mg = Migrate()


def create_app():    
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    
    db.init_app(app)       

    mg.init_app(app, db)
    views.init_app(app)

    with app.app_context():
       db.create_all()  

    return app
