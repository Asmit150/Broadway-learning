import psycopg2


def estd_connection():
    conn = psycopg2.connect(
        database="student",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor
