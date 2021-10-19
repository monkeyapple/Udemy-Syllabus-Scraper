from configparser import ConfigParser
import os


def read_config():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'database.ini')
    # create a parser
    config = ConfigParser()
    # read config file
    config.read(file_path)

    # this function will return a dictionary with keys set in database.ini
    return config

def connection_uri():
    config=read_config()
    print(config)
    DB_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        config['udemy-scrape-postgresql']['user'],
        config['udemy-scrape-postgresql']['password'],
        config['udemy-scrape-postgresql']['host'],
        config['udemy-scrape-postgresql']['port'],
        config['udemy-scrape-postgresql']['dbname']
    )
    return DB_URI


