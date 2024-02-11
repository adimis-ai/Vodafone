import os
import sqlite3

class DBConnector:
    def __init__(self, db_file):
        self.db_file = db_file
        self.client = self._connect()

    def _connect(self):
        try:
            db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', self.db_file))
            print("Db Path: ", db_path)
            if not os.path.exists(db_path):
                print("Database file does not exist. Creating a new one.")
            return sqlite3.connect(db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close(self):
        if self.client:
            self.client.close()
            print("Connection to database closed")

    def get_db_client(self):
        return self.client

# Example usage:
if __name__ == "__main__":
    connector = DBConnector('example.db')
    if connector.get_db_client():
        connector.get_db_client().execute("SELECT * FROM users")
        connector.close()
    else:
        print("Failed to establish connection to the database.")
