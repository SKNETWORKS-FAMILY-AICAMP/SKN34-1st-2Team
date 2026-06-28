import config as cf

class Database:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        return cf.DB_HOST
    
db = Database()