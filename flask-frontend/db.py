from configparser import ConfigParser
def read_config(filename='database.ini'):
    # create a parser
    config = ConfigParser()
    # read config file
    config.read(filename)

    # this function will return a dictionary with keys set in database.ini
    return config

def connection_uri():
    config=read_config()
    DB_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    config['udemy-scrape-postgresql']['user'],
    config['udemy-scrape-postgresql']['password'],
    config['udemy-scrape-postgresql']['host'],
    config['udemy-scrape-postgresql']['port'],
    config['udemy-scrape-postgresql']['dbname']
    )
    return DB_URI
