from data.db import get_db

def insert_user(name, username, email):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(name, username, email) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, username, email])
    db.commit()
    return True

def update_user(id, name, username, email):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE users SET name = ?, username = ?, email = ? WHERE id = ?"
    cursor.execute(statement, [name, username, email, id])
    db.commit()
    return True

def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, username, email FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, username, email FROM users"
    cursor.execute(query)
    return cursor.fetchall()