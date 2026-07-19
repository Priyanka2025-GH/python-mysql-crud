

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="p1"
)

cursor = conn.cursor()

print("Database Connected Successfully")

def check_username(username):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()

def insert_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    conn.commit()

def login_user(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    return cursor.fetchone()

def get_user(username):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()

def update_user(old_username, new_username, new_password):
    query = "UPDATE users SET username=%s, password=%s WHERE username=%s"
    cursor.execute(query, (new_username, new_password, old_username))
    conn.commit()

def delete_user(username):
    query = "DELETE FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    conn.commit()