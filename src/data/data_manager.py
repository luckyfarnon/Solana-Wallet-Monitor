from .database import Database  # Import Database class

class DataManager:
    def __init__(self, db_file):
        self.database = Database(db_file)
        self.database.create_table()  # Ensure the table is created

    def add_trade(self, token_address, amount):
        # Add trade to the database
        self.database.insert_trade(token_address, amount)

    def close(self):
        self.database.close_connection()

