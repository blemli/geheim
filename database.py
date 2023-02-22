import os

import psycopg2


def _connect(connection_string):
    connection = None
    try:
        connection = psycopg2.connect(connection_string)
        print("Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def _execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
        try:
            result = cursor.fetchall()
            return result
        except psycopg2.ProgrammingError as e:
            print(f"{e}")
            return None
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")


def init(db):
	create_secrets_query = """
CREATE TABLE IF NOT EXISTS secrets (
  id UUID PRIMARY KEY NOT NULL,
  ciphertext TEXT NOT NULL,
  saved DATE NOT NULL DEFAULT CURRENT_DATE
);
"""
	_execute_query(db, create_secrets_query)


def get_tables(db):
    query = """SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;"""
    return _execute_query(query)


def test():
    db = _connect(os.environ['DB_CONNECTION'])
    init(db)
    return get_tables(db)
