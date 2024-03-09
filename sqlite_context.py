import sqlite3

class SqliteConnection:

    def __init__(self, host):
        self.host=host
        self.connection=None

    def __enter__(self):
        self.connection=sqlite3.connect('underwriter.db')
        return self.connection  #we are returing the connection object

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.connection.commit()
        self.connection.close()
