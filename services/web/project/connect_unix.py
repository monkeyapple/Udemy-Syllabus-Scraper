# services/web/project/connect_unix.py
import os

def get_connect_url():
    db_user = os.environ["DB_USER"]  # e.g. 'my-database-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-database-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    if "INSTANCE_UNIX_SOCKET" in os.environ:
        unix_socket_path = os.environ["INSTANCE_UNIX_SOCKET"]  # e.g. '/cloudsql/project:region:instance'
        return f"postgresql+pg8000://{db_user}:{db_pass}@/{db_name}?unix_sock={unix_socket_path}/.s.PGSQL.5432"
    else:
        # Local test
        db_host=os.environ["DB_HOST"]
        db_port=os.environ["DB_PORT"]
        return f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
       
