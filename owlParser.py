import rdflib
from abstractmodel import AbstractModel


def remove_string(to_edit):
    subject_to_remove = 'http://www.radlex.org/RID/#'
    return to_edit.replace(subject_to_remove, '')


def parse():
    owl_file = "RadlexSmall.owl"
    g = rdflib.Graph()
    g.load(owl_file)

    m = AbstractModel()
    i = 0
    for subject, predicate, obj in g:
        if "Preferred_name" in predicate:
            # print(str(i) + " pref " + remove_string(str(subject)) + " " + str(predicate) + " " + str(obj))
            m.add_name(remove_string(str(subject)), remove_string(str(obj)))

        elif "Synonym" in predicate:
            #print(str(i) + " syn " + remove_string(str(subject)) + " " + str(predicate) + " " + str(obj))
            m.add_syn(remove_string(str(subject)), remove_string(str(obj)))

        i+=1
    print("end ")

    filename = 'this.txt'
    m.save(filename)





if __name__ == '__main__':
    parse()