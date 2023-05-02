class Config(object):

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{database}'.format(
        user = 'bookish', 
        password = 'bookish', 
        host = 'localhost', 
        database = 'bookish', 
    )
