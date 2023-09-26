# database_handler.py

import sqlite3

def connect_to_database():
    try:
        conn = sqlite3.connect("obs_db.db")
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(e)
        return None, None

def create_tables():
    conn, cursor = connect_to_database()
    if conn:
        create_table = '''CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT
        );'''
        create_admin = '''CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT UNIQUE,
            pwd TEXT
        );'''
        cursor.execute(create_table)
        cursor.execute(create_admin)
        conn.commit()
        conn.close()
    else:
        print("Veritabanına bağlanılamadı.")

def login(username, password):
    conn, cursor = connect_to_database()
    if conn:
        cursor.execute('SELECT * FROM admins WHERE name = ? AND pwd = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    else:
        print("Veritabanına bağlanılamadı.")
        return None

def add_student(name, surname, email, phone):
    try:
        conn = sqlite3.connect("obs_db.db")
        cursor = conn.cursor()

        insert_query = "INSERT INTO students (name, surname, email, phone) VALUES (?, ?, ?, ?)"
        student_data = (name, surname, email, phone)

        cursor.execute(insert_query, student_data)
        conn.commit()

        print("Öğrenci başarıyla eklendi!")

        conn.close()

    except sqlite3.Error as e:
        print("Öğrenci eklenirken bir hata oluştu:", e)

def get_students():
    try:
        conn = sqlite3.connect("obs_db.db")
        cursor = conn.cursor()

        select_query = "SELECT student_id, name, surname, email, phone FROM students"
        cursor.execute(select_query)
        students = cursor.fetchall()

        conn.close()

        return students

    except sqlite3.Error as e:
        print("Öğrenciler alınırken bir hata oluştu:", e)
        return []
