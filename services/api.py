import config as cf

class Api:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        return cf.API_KEY
    
api = Api()