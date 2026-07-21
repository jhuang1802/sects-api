import sqlite3
from fastapi import HTTPException
import datetime as dt

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shows (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            city TEXT,
            venue TEXT
            );
        """)

def get_connection():
    conn = sqlite3.connect('shows.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_shows():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * from shows ORDER BY id DESC""")
        rows = cursor.fetchall()
    
    return rows

def add_show(date: dt.date, city: str, venue:str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO shows (date, city, venue) VALUES (?, ?, ?) RETURNING *""", (date, city, venue))
        row = cursor.fetchone()
    return row