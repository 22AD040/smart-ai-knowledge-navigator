import sqlite3

def create_db():

    conn=sqlite3.connect("database/users.db")
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    email TEXT PRIMARY KEY,
    password TEXT
    )
    """)

    conn.commit()
    conn.close()