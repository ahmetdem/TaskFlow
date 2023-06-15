from flask import g
import sqlite3

def get_number_of_user(conn) -> int:
    """
    Get number of users that is registered to database.
    """
    c = conn.cursor()

    with conn:
        c.execute("SELECT COUNT(*) FROM tasks")
        result = c.fetchone()[0]
        return result
    

def insert_database(conn, title: str, content: str) -> None:
    """
    Insert task to database.
    """
    c = conn.cursor()
    id = get_number_of_user(conn) + 1
    
    with conn:
        c.execute("INSERT INTO tasks VALUES (:id, :title, :content, :complated)", {'id': id, 'title': title, 'content': content, 'complated': 0})


def get_db():
    """
    Set the database connection.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('tasks.db')

    return db


def close_connection(exception):
    """
    Close the database connection.
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    """
    Send query to database.
    """
    db = get_db()
    cursor = db.execute(query, args)
    rv = cursor.fetchall()
    db.commit()
    cursor.close()
    return (rv[0] if rv else None) if one else rv


if __name__ == '__main__':
    insert_database('test4', 'test4')
    insert_database('test5', 'test5')
    insert_database('test6', 'test6')

