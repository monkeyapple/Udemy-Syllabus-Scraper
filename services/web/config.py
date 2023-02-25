import os

class Config:
    # Replace 'postgresql' with 'postgres' if you're using a PostgreSQL version below 9.3
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
