from .app import app
import psycopg2


def main():
    _create_postgres_database()
    app.run()

def _create_postgres_database():
    conn = psycopg2.connect(
        dbname='bookish', # this needs to be defined to establish a server connection
        host='localhost',
        port='5432',
        user='bookish',
        password='bookish'
    )
    cursor = conn.cursor()
    conn.autocommit = True
    try:
        cursor.execute('CREATE DATABASE bookish')
    except psycopg2.errors.DuplicateDatabase:
        print('Database bookish already exists, skipping creation.')
    cursor.close()
    conn.close()
