from flask import Flask
# from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
# Talisman(app, content_security_policy=None)

app.config.from_object("project.config.Config")

db = SQLAlchemy(app)
db.create_all()

from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
