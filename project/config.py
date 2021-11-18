import os
SECRET_KEY = os.urandom (256)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# GCP
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = ''
CLOUDSQL_DATABASE = ''
CLOUDSQL_CONNECTION_NAME = ''
DB_SOCKET_DIR=''
INSTANCE_CONNECTION_NAME=''

LIVE_SQLALCHEMY_DATABASE_URI = (
    "postgresql+pg8000://{username}:{password}@/{database}?unix_sock={db_socket_dir}/{instance_connection_name}/.s.PGSQL.5432").format (
    username=CLOUDSQL_USER,
    password=CLOUDSQL_PASSWORD,
    database=CLOUDSQL_DATABASE,
    db_socket_dir=DB_SOCKET_DIR,
    instance_connection_name=INSTANCE_CONNECTION_NAME,
)

SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI

