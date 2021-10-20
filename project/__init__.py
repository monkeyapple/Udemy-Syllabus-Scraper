from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_session import Session
from flask_caching import Cache
import os
import pylibmc

app=Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = os.environ.get('SECRET_KEY'),
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

cache = Cache()
cache_servers = os.environ.get('MEMCACHIER_SERVERS')
if cache_servers == None:
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})
else:
    cache_user = os.environ.get('MEMCACHIER_USERNAME') or ''
    cache_pass = os.environ.get('MEMCACHIER_PASSWORD') or ''
    app.config.update(
        SESSION_TYPE = 'memcached',
        SESSION_MEMCACHED =
            pylibmc.Client(cache_servers.split(','), binary=True,
                            username=cache_user, password=cache_pass,
                            behaviors={
                                # Faster IO
                                'tcp_nodelay': True,
                                # Keep connection alive
                                'tcp_keepalive': True,
                                # Timeout for set/get requests
                                'connect_timeout': 2000, # ms
                                'send_timeout': 750 * 1000, # us
                                'receive_timeout': 750 * 1000, # us
                                '_poll_timeout': 2000, # ms
                                # Better failover
                                'ketama': True,
                                'remove_failed': 1,
                                'retry_timeout': 2,
                                'dead_timeout': 30,
                            })
    )


############################################
        # SQL DATABASE
##########################################

db = SQLAlchemy(app)
Migrate(app,db)
Markdown(app)
Session(app)

from project.udemy.views import index_blueprint
app.register_blueprint(index_blueprint,url_prefix='/')
