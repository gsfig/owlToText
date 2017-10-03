import rdflib
import json
import sqlite3
from abstractmodel import AbstractModel


def remove_string(to_edit):
    subject_to_remove = 'http://www.radlex.org/RID/#'
    return to_edit.replace(subject_to_remove, '')


def parse(m):
    # TODO: try to add "label" to list to extract and then add in list of what to Print
    with open('config.json') as data_file:
        config = json.load(data_file)

    print(config)

    g = rdflib.Graph()
    g.load(config["owl_file"])
    # m = AbstractModel()
    for subject, predicate, obj in g:
        for tag in config["tags_to_extract_in_predicate"]:
            if tag in predicate:
                m.addinMemory(remove_string(str(subject)), remove_string(str(obj)), tag)
    # m.print_to_file(config["out_filename"])

    # m.print(config["out_filename"])


def testdb(config):
    db_name = config["db_name"]
    connection = sqlite3.connect(db_name)

    r = connection.execute('''SELECT COUNT(*) FROM owlEntity''')
    p(r, "owlEntities")
    r = connection.execute('''SELECT COUNT(*) FROM Preferred_name''')
    p(r, "Preferred_name")
    r = connection.execute('''SELECT COUNT(*) FROM Synonym''')
    p(r, "Synonym")
    r = connection.execute('''SELECT COUNT(*) FROM Preferred_Name_for_Obsolete''')
    p(r, "Preferred_Name_for_Obsolete")
    r = connection.execute('''SELECT COUNT(*) FROM SNOMED_Term''')
    p(r, "SNOMED_Term")
    r = connection.execute('''SELECT COUNT(*) FROM UMLS_Term''')
    p(r, "UMLS_Term")

    connection.close()


def p(rows, s):
    print(s)
    for row in rows:
        for ritem in row:
            print(ritem)


def from_file(config_f, m):

    with open(config_f["out_filename"]) as file:
        data = json.load(file)

    for id in data:
        for tag in data[id]:
            for item in data[id][tag]:
                print(id + " " + item + " " + tag)
                m.addinMemory(str(id), str(item), tag)


if __name__ == '__main__':
    with open('config.json') as config_file:
        config = json.load(config_file)

    models = AbstractModel()

    # from_file(config, models)
    # m.printPredicates()
    #parse(models)
    #models.print_to_file(config["out_filename"])
    # models.save_to_db()

    testdb(config)

    #models.close_connection()





    # m.appendNamesForNer()
