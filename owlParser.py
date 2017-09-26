import rdflib
import json
import re

from abstractmodel import AbstractModel


def remove_string(to_edit):
    subject_to_remove = 'http://www.radlex.org/RID/#'
    return to_edit.replace(subject_to_remove, '')


def parse():
    #TODO: try to add "label" to list to extract and then add in list of what to Print
    with open('config.json') as data_file:
        config = json.load(data_file)

    #pprint(config)

    g = rdflib.Graph()
    g.load(config["owl_file"])
    m = AbstractModel()
    for subject, predicate, obj in g:
        for tag in config["tags_to_extract_in_predicate"]:
            if tag in predicate:
                m.add(remove_string(str(subject)), remove_string(str(obj)), tag)

    m.print(config["out_filename"])


def printPredicates():
    with open('config.json') as data_file:
        config = json.load(data_file)
    g = rdflib.Graph()
    g.load(config["owl_file"])
    pred = list()
    i = 0
    for subject, predicate, obj in g:
        if predicate not in pred:
            pred.append(predicate)
            print(str(predicate))
            i+=1
    print("has " + str(i) + " predicates")


def appendNamesForNer():
    with open('config.json') as data_file:
        config = json.load(data_file)
    file_read = config["out_filename"]
    filename = config["lexicon_filename"]
    filewrite = open(filename, "w")
    with open(file_read, "r") as read:
        json_read = json.load(read)

    out = list()

    for rid in json_read:
        for tag in json_read[rid]:
            for item in json_read[rid][tag]:
                #out.append(item + " " + rid + " " +tag)
                out.append(item)

    out.sort()
    for s in out:
        filewrite.write(s)
        filewrite.write("\n")

    data_file.close()
    read.close()
    filewrite.close()


if __name__ == '__main__':
    #printPredicates()
    parse()
    appendNamesForNer()
