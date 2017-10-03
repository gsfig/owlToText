import json
import sqlite3


class ModeltoDB:
    db_name = ''
    connection = ''

    #def __init__(self):
        #self.create()

    def create(self):

        with open('config.json') as config_file:
            config = json.load(config_file)

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


        for tag in config["tags_to_extract_in_predicate"]:
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
                  INSERT INTO owlEntity(name) VALUES (?)''', (name,))
            self.connection.commit()
            rows = self.connection.execute('SELECT id FROM owlEntity WHERE name = ?', (name,))
            for row in rows:
                entry = row[0]
            for tag in data[name]:
                for item in data[name][tag]:
                    table_name_col = tag+" (name, fkentity)"
                    self.connection.execute(''' INSERT INTO '''+table_name_col+''' VALUES (?,?)''', (item, entry,))
                    self.connection.commit()

    def connect_existing(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
        self.db_name = config["db_name"]
        self.connection = sqlite3.connect(self.db_name)

    def close_connection(self):
        self.connection.close()

    def check_exists(self, id):
        raise NotImplementedError("error message")

    def print(self, filename):
        raise NotImplementedError("error message")

    def printPredicates(self):
        raise NotImplementedError("error message")

    def appendNamesForNer(self):
        raise NotImplementedError("error message")