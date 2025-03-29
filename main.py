from db_functions import *


if __name__ == '__main__':
    db_file = "campervan_database.db"
    conn = create_connection("campervan_database.db")
    if conn is not None:
        execute_sql(conn, create_topics_sql)
        execute_sql(conn, create_steps_sql)
        execute_sql(conn, create_howtos_sql)
        add_column(conn, "topics", "Name", "varchar(255)")
        conn.close()

