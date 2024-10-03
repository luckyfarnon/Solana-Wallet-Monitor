# data_manager.py

from database import Database
from utils.logging_utils import logger

class DataManager:
    def __init__(self, db_file):
        self.database = Database(db_file)
        self.database.create_table()

    def add_trade(self, token_address, amount):
        self.database.insert_trade(token_address, amount)

    def close(self):
        self.database.close_connection()
