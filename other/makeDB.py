import sqlite3


class MakeDB:

    # example = want to remove from http://www.radlex.org/RID/#RID3545 to keep the term id
    subject_toRemove = 'http://www.radlex.org/RID/#'
    connection = None
    c = None
    db_file = "radlex.db"

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)
        self.c = self.connection.cursor()

    def removetrailing(self, string):
        return string.replace(self.subject_toRemove, '')

    def createDB(self):
        self.c.execute('''
                  DROP TABLE IF EXISTS entity
                  ''')

        self.c.execute('''
                  CREATE TABLE entity (
                  id     INTEGER PRIMARY KEY AUTOINCREMENT,
                  name         VARCHAR(255),
                  idlink          VARCHAR(10),
                  UNIQUE (idlink)
                  )''')


    def add(self, subject, predicate, obj):
        s = self.removetrailing(subject)

        self.c.execute('''
                  INSERT OR IGNORE INTO entity (name,idlink) VALUES (?,?)
                 ''', (obj, s,))







