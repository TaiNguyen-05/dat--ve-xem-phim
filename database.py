import sqlite3

def connect():
    return sqlite3.connect("user.db")

def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            role TEXT CHECK(role IN ('admin', 'nhanvien', 'khachhang')) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    pass
