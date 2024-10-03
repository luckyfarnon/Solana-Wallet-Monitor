import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(self):
        # Create tables for storing transaction history, token detection logs, and trade logs
        create_trade_table_sql = '''CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token_address TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );'''
        try:
            c = self.connection.cursor()
            c.execute(create_trade_table_sql)
        except Error as e:
            print(e)

    def insert_trade(self, token_address, amount):
        sql = '''INSERT INTO trades(token_address, amount) VALUES(?, ?)'''
        cur = self.connection.cursor()
        cur.execute(sql, (token_address, amount))
        self.connection.commit()
        return cur.lastrowid

    def close_connection(self):
        if self.connection:
            self.connection.close()
