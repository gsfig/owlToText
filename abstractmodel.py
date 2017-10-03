from modelImplementation.inMemory import ModelinMemory
from modelImplementation.sqlite3DB import ModeltoDB
from modelImplementation.inFile import ModelinFile


class AbstractModel:
    m_mem = ''
    m_db = ''
    m_file = ''

    def __init__(self, db_name):
        self.m_mem = ModelinMemory()
        self.m_db = ModeltoDB(db_name)
        self.m_file = ModelinFile()

    def addinMemory(self, subj, obj, tag):
        """
        Adds subject, object and predicate to data structure.
        Guarantees subjects are unique.

        :param subj:
        :param obj:
        :param tag:
        :return:
        """

        self.m_mem.add(subj, obj, tag)

    def get_data(self):
        """
        Gets data stored temporarily in memory
        :return: data structure
        """
        if self.m_mem.data is None:
            raise NameError("data not added yet")
        else:
            return self.m_mem.data

    def save_to_db(self):
        """
        Saves data from memory to database
        :return:
        """
        self.m_db.save(self.get_data())

    def create_db(self, pred_list):
        """
        Creates database
        :return:
        """
        self.m_db.create(pred_list)

    def connect_existing(self):
        """
        Connects to existing database file
        :return: True if connection successful; False if not successful
        """
        return self.m_db.connect_existing()

    def close_connection(self):
        """
        Closes database connection
        :return:
        """
        self.m_db.close_connection()

    def check_exists(self, id):
        """
        Checks if id exists in data
        :param id: identifier to look for
        :return: True or False
        """
        self.m_mem.check_exists(id)

    def from_file(self, file_path):
        """
        From file , adds subject, object and predicates
        :param file_path: json config file
        :return:
        """
        self.m_mem.from_file(file_path)

    def print_to_file(self, filename):
        """
        Saves data to file
        :param filename: path to save data
        :return:
        """
        self.m_file.print_to_json_file(self.get_data(), filename)

    def printPredicates(self, owl_file):
        """
        Prints all the predicates that exist in owl file
        :param owl_file: owl file to extract predicates
        :return:
        """
        self.m_file.printPredicates(owl_file)

    def appendNamesForNer(self, out_filename, lexicon_filename):
        """
        Creates file with list of names, one per line, useful for NER extraction
        :param out_filename: file with data
        :param lexicon_filename:
        :return:
        """
        self.m_file.appendNamesForNer(out_filename, lexicon_filename)


