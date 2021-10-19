from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_session import Session
from flask_caching import Cache
import os

app=Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

#####################################
    #Memcache for session storage#
#####################################

############################################
        # SQL DATABASE
##########################################

db = SQLAlchemy(app)
Migrate(app,db)
Markdown(app)


from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
