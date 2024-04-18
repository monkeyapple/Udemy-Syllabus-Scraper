# services/web/project/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pg8000
from project.connect_unix import get_connect_url
import os

app=Flask(__name__)
# Talisman(app, content_security_policy=None)

app.config["SQLALCHEMY_DATABASE_URI"] = get_connect_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_POOL_SIZE"]=5
app.config["SQLALCHEMY_MAX_OVERFLOW"]=10
app.config["SQLALCHEMY_POOL_RECYCLE"]=280

db = SQLAlchemy(app)


from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
