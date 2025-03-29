import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
    except Error as error:
        print(error)
    return conn


def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as error:
        print(error)

def add_column(conn, table, column_name, column_type):
    sql = f"ALTER TABLE {table} ADD COLUMN {column_name} {column_type}"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(f"'{column_name}' column was added to '{table}' table.")


create_topics_sql = """
CREATE TABLE IF NOT EXISTS topics (
TopicID integer PRIMARY KEY,
Area varchar(255) NOT NULL,
PersonResponsible1 varchar(255) NOT NULL,
PersonResponsible2 varchar(255)
);
"""

create_steps_sql = """
CREATE TABLE IF NOT EXISTS steps (
StepID integer PRIMARY KEY,
Name varchar(255) NOT NULL,
Description varchar(255),
TopicID integer NOT NULL,
Deadline text NOT NULL,
FOREIGN KEY (TopicID) REFERENCES topics(TopicID)
);
"""

create_howtos_sql = """
CREATE TABLE IF NOT EXISTS howtos (
HowtoID integer PRIMARY KEY,
Name varchar(255) NOT NULL,
Tools varchar(255),
SME varchar(255),
Steps varchar(255),
FOREIGN KEY (Steps) REFERENCES steps(Name)
);
"""
