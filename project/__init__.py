from flask import Flask
from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app=Flask(__name__)
Talisman(app, content_security_policy=None)

app.config.from_mapping(
    SECRET_KEY = os.environ.get('SECRET_KEY'),
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1),
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False, 
)

############################################
        # SQL DATABASE
##########################################

db = SQLAlchemy(app)
Migrate(app,db)

db.create_all()

from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
