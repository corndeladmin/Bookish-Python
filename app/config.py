import os

class Config(object):
    SECRET_KEY = 'secret-key'

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{database}'.format(
        user = 'bookish', 
        password = 'bookish', 
        host = 'localhost', 
        database = 'bookish', 
    )
