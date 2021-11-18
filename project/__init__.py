from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
<<<<<<< Updated upstream
from flaskext.markdown import Markdown
from project.udemy.storage import connection_uri
=======
import os
from project import config
>>>>>>> Stashed changes

app=Flask(__name__)
Markdown(app)

<<<<<<< Updated upstream
app.config['SECRET_KEY']='onlinecoursesecretkey'
=======
#heroku & local test
# app.config.from_mapping(
#     SECRET_KEY = os.environ.get('SECRET_KEY'),
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1),
#     SQLALCHEMY_TRACK_MODIFICATIONS = False, 
# )
>>>>>>> Stashed changes

#GCP
app.config.from_object (config)
############################################

        # SQL DATABASE AND MODELS

##########################################

DB_URI = connection_uri()

app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
