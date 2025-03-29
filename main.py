from db_functions import *


if __name__ == '__main__':
    db_file = "campervan_database.db"
    conn = create_connection("campervan_database.db")
    conn.execute('PRAGMA foreign_keys = ON;')

    if conn is not None:
        execute_sql(conn, create_topics_sql)
        execute_sql(conn, create_steps_sql)
        execute_sql(conn, create_howtos_sql)

        add_column(conn, "topics", "Name", "varchar(255)")
        topic = (1, "Water system", "Ola", "-", "Outdoor shower")
        topic_id = add_topic(conn, topic)
        step = (1,
                "Rearrange pipes",
                "Increase the length of the outdoor shower pipe",
                topic_id,
                "2025-06-20 00:00:00")
        step_id = add_step(conn, step)
        howto = (1,
                 "Dividing the pipe",
                 "Pipe splitter",
                 "Obi Van Kenobi",
                 step_id)
        howto_id = add_howto(conn, howto)
        print(f"Inserted Topic ID: {topic_id}, Step ID: {step_id}, Howto ID: {howto_id}")

        select_topic_by_area(conn, "Water system")
        select_all(conn, "howtos")

        update(
            conn,
            "steps",
            "Rearrange pipes",
            Description="Increase the length and the diameter of the outdoor shower pipe"
        )

        delete_all(conn, "howtos")
        conn.close()
