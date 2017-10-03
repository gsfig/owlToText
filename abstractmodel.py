from modelImplementation.inMemory import ModelinMemory
from modelImplementation.db import ModeltoDB
from modelImplementation.toFile import ModeltoFile


class AbstractModel:
    m_mem = ModelinMemory()
    m_db = ModeltoDB()
    m_file = ModeltoFile()

    def addinMemory(self, subj, obj, tag):
        self.m_mem.add(subj, obj, tag)

    def get_data(self):
        if self.m_mem.data is None:
            raise NameError("data not added yet")
        else:
            return self.m_mem.data

    def save_to_db(self):
        self.m_db.save(self.get_data())

    def create_db(self):
        self.m_db.create()

    def connect_existing(self):
        self.m_db.connect_existing()

    def close_connection(self):
        self.m_db.close_connection()

    def check_exists(self, id):
        self.m_mem.check_exists(id)

    def print_to_file(self, filename):
        self.m_file.print_to_file(self.get_data(), filename)

    def printPredicates(self):
        self.m_file.printPredicates()

    def appendNamesForNer(self):
        self.m_file.appendNamesForNer()


