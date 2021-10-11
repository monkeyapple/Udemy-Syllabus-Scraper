from configparser import ConfigParser
def config(filename='database.ini'):
    # create a parser
    db = ConfigParser()
    # read config file
    db.read(filename)

    # this function will return a dictionary with keys set in database.ini
    return db

    