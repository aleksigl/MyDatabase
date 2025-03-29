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


if __name__ == '__main__':

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

    db_file = "campervan_database.db"
    conn = create_connection("campervan_database.db")
    if conn is not None:
        execute_sql(conn, create_topics_sql)
        execute_sql(conn, create_steps_sql)
        execute_sql(conn, create_howtos_sql)
        conn.close()
