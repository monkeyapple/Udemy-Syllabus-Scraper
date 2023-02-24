import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'../../.env'))

class Config(object):
    # Use the Cloud SQL Proxy to connect to the Cloud SQL instance
    # SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@/{os.environ['DB_NAME']}?host=/cloudsql/{os.environ['CLOUD_SQL_CONNECTION_NAME']}"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False