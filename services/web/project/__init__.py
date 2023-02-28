# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import pg8000


# app=Flask(__name__)
# # Talisman(app, content_security_policy=None)

# app.config.from_object("project.config.Config")

# db = SQLAlchemy(app)

# from project.udemy.views import index_blueprint
# app.register_blueprint(index_blueprint,url_prefix='/')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pg8000
from project.connect_unix import get_connect_url
import os

app=Flask(__name__)
# Talisman(app, content_security_policy=None)

app.config["SQLALCHEMY_DATABASE_URI"] = get_connect_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)


from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
