import rdflib
import json
import sqlite3
from abstractmodel import AbstractModel


def remove_string(to_edit):
    # TODO: use json config to get remove string
    subject_to_remove = 'http://www.radlex.org/RID/#'
    return to_edit.replace(subject_to_remove, '')


def parse(owl_f, pred_list, m):
    """
    From an owl file parses subject and objects from each predicate to extract

    :param owl_f: owl file path
    :param pred_list: list of predicates to extract
    :param m: model class
    :return:
    """

    g = rdflib.Graph()
    g.load(owl_f)
    for subject, predicate, obj in g:
        for tag in pred_list:
            if tag in predicate:
                m.addinMemory(remove_string(str(subject)), remove_string(str(obj)), tag)

    print("added to memory")


def testdb(db_name):
    connection = sqlite3.connect(db_name)

    res = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Database table names and number of entries:")
    for name in res:
        table_name = name[0]
        r = connection.execute('''SELECT COUNT(*) FROM '%s' ''' % table_name)
        print(table_name + " " + str(r.fetchall()[0]))

    connection.close()


if __name__ == '__main__':

    ''' 
    1. setup 
    '''
    with open('config.json') as config_file:
        config = json.load(config_file)
    dbName = config["database_path"] + config["db_name"]
    owl_file = config["files_path"] + config["owl_file"]
    predicate_list = config["tags_to_extract_in_predicate"]

    models = AbstractModel(dbName)

    ''' 
    1.1. check to change json config file predicates 
    '''
    # models.printPredicates(owl_file)

    ''' 
    1.2. connect or create database 
    '''
    if not models.connect_existing():
        models.create_db(predicate_list)

    ''' 
    2. owl to memory 
    '''
    parse(owl_file, predicate_list, models)

    ''' 
    3.1. files 
    '''
    # json_file = config["output_path"] + config["out_filename"]
    # lexicon_file = config["output_path"] + config["lexicon_filename"]
    # models.print_to_file(json_file)
    # models.appendNamesForNer(json_file, lexicon_file)

    ''' 
    3.2 from file to memory, Should be quicker than 2. owl -> memory 
    '''
    # models.from_file(json_file)

    ''' 
    4. save from memory to database 
    '''
    models.save_to_db()

    ''' 
    simple test 
    '''
    # testdb(dbName)

    ''' 
    5. close connection 
    '''
    models.close_connection()
