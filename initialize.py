import database as db


def initialize_db():
    overwrite = ""  # "IF NOT EXISTS"
    create_secrets_query = """
CREATE TABLE {overwrite} secrets (
  id VARCHAR PRIMARY KEY NOT NULL,
  ciphertext TEXT NOT NULL,
  saved DATE NOT NULL DEFAULT CURRENT_DATE
);
"""
    db._execute_query(create_secrets_query)


def get_tables():  # todo: remove?
    query = """SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;"""
    return db._execute_query(query)


if __name__ == "__main__":
    initialize_db()
    print(db.test())
