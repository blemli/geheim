import os
import psycopg2


def _connect(connection_string):
    connection = None
    try:
        connection = psycopg2.connect(connection_string)
        print("Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print(f"could not connect to databse: '{e}'")
    return connection


def _execute_query(query, data=None):
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


def init():
    create_secrets_query = """
CREATE TABLE IF NOT EXISTS secrets (
  id UUID PRIMARY KEY NOT NULL,
  ciphertext TEXT NOT NULL,
  saved DATE NOT NULL DEFAULT CURRENT_DATE
);
"""
    _execute_query(create_secrets_query)


def get_tables():  # todo: remove?
    query = """SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;"""
    return _execute_query(query)


def store_secret(id, secret):
    insert_query = (
        f"INSERT INTO secrets (id, ciphertext) VALUES {id,secret}"
    )
    _execute_query(insert_query)


def retrieve_secret(id):
    select_query = f"SELECT ciphertext FROM secrets WHERE id = {id}"
    return _execute_query(select_query)


def cleanup():
    pass  # todo: implement


connection = _connect(os.environ['DB_CONNECTION'])


def test():
    store_secret(123, "gaga")
    return retrieve_secret(123)
