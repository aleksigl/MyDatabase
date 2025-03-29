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
Step integer,
FOREIGN KEY (Step) REFERENCES steps(StepID)
);
"""


def add_column(conn, table, column_name, column_type):
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    columns = cur.fetchall()

    if any(column[1] == column_name for column in columns):
        print(f"Column '{column_name}' already exists in table '{table}'. Skipping addition.")
        return

    sql = f"ALTER TABLE {table} ADD COLUMN {column_name} {column_type}"
    try:
        cur.execute(sql)
        conn.commit()
        print(f"'{column_name}' column was added to '{table}' table.")
    except Error as error:
        print(error)


def add_topic(conn, topic):
    sql = """INSERT INTO topics(TopicID, Area, PersonResponsible1, PersonResponsible2, Name)
                VALUES (?, ?, ?, ?, ?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, topic)
        conn.commit()
        return cur.lastrowid
    except Error as error:
        print(error)


def add_step(conn, step):
    sql = """INSERT INTO steps(StepID, Name, Description, TopicID, Deadline)
                VALUES (?, ?, ?, ?, ?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, step)
        conn.commit()
        return cur.lastrowid
    except Error as error:
        print(error)


def add_howto(conn, howto):
    sql = """INSERT INTO howtos(HowtoID, Name, Tools, SME, Step)
                VALUES (?, ?, ?, ?, ?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, howto)
        conn.commit()
        return cur.lastrowid
    except Error as error:
        print(error)


def select_topic_by_area(conn, area):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE Area=?", (area,))
        rows = cur.fetchall()
        return rows
    except Error as error:
        print(error)


def select_all(conn, table):
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        return rows
    except Error as error:
        print(error)


def update(conn, table, id, **kwargs):
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id,)

    sql = f""" UPDATE {table}
             SET {parameters}
             WHERE Name = ?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except Error as error:
        print(error)


def delete_all(conn, table):
    sql = f"DELETE FROM {table}"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(f"{table} deleted.")
