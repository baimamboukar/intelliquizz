class IntelliquizzDB():
    def __init__(self):
        self.db = None

    def connect(self):
        import sqlite3
        if(self.db == None):
            self.db = sqlite3.connect('static/intelliquizz.sqlite')
        return self.db

    def get_cursor(self):
        return self.db.cursor()
    
    def close(self):
        self.db.close()