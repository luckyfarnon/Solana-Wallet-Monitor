# database.py

import sqlite3
from sqlite3 import Error
from utils.logging_utils import logger

class Database:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            logger.info(f'Connected to database: {db_file}')
        except Error as e:
            logger.error(f'Error connecting to database: {e}')
        return conn

    def create_table(self):
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token_address TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            logger.info('Trades table created')
        except Error as e:
            logger.error(f'Error creating table: {e}')

    def insert_trade(self, token_address, amount):
        sql = '''INSERT INTO trades(token_address, amount) VALUES(?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (token_address, amount))
            self.connection.commit()
            logger.info(f'Trade inserted: {token_address}, {amount}')
        except Error as e:
            logger.error(f'Error inserting trade: {e}')

    def close_connection(self):
        if self.connection:
            self.connection.close()
            logger.info('Database connection closed')
