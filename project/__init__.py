from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from project.udemy.storage import connection_uri

app=Flask(__name__)
Markdown(app)

app.config['SECRET_KEY']='onlinecoursesecretkey'

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
