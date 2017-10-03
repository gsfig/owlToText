import json
import sqlite3
from os.path import isfile, getsize


class ModeltoDB:
    db_name = ''
    connection = ''

    def __init__(self, db):
        self.db_name = db

    def create(self, predicate_list):

        print("creating database")

        self.connection = sqlite3.connect(self.db_name)

        self.connection.isolation_level = None  # auto_commit
        c = self.connection.cursor()
        self.connection.execute('''
                  DROP TABLE IF EXISTS owlEntity
                  ''')

        self.connection.execute('''
                  CREATE TABLE owlEntity (
                  id     INTEGER PRIMARY KEY AUTOINCREMENT,
                  name   VARCHAR(100) UNIQUE
                  )''')

        for tag in predicate_list:
            self.connection.execute('''
                              DROP TABLE IF EXISTS '%s'
                              ''' % tag)
            self.connection.execute('''
                  CREATE TABLE '%s' (
                  id     INTEGER PRIMARY KEY AUTOINCREMENT,
                  name   VARCHAR(100),
                  fkentity   INTEGER,
                  FOREIGN KEY(fkentity) REFERENCES owlEntity(id)
                  )
                  ''' % tag)

    def save(self, data):

        for name in data:
            self.connection.execute('''
                  INSERT OR IGNORE INTO owlEntity(name) VALUES (?)''', (name,))
            self.connection.commit()
            rows = self.connection.execute('SELECT id FROM owlEntity WHERE name = ?', (name,))
            for row in rows:
                entry = row[0]
            for tag in data[name]:
                for item in data[name][tag]:
                    table_name_col = tag+" (name, fkentity)"
                    self.connection.execute(''' INSERT INTO '''+table_name_col+''' VALUES (?,?)''', (item, entry,))
                    self.connection.commit()

        print("saved data to " + self.db_name)

    def connect_existing(self):
        if isfile(self.db_name):
            if getsize(self.db_name) > 100:
                with open(self.db_name, 'r', encoding="ISO-8859-1") as f:
                    header = f.read(100)
                    if header.startswith('SQLite format 3'):
                        self.connection = sqlite3.connect(self.db_name)
                        print("SQLite3 database has been detected.")
                        return True

        else:
            print("no database detected")
            return False

    def close_connection(self):
        self.connection.close()

    def check_exists(self, id):
        raise NotImplementedError("error message")
