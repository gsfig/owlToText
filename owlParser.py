import rdflib
from abstractmodel import AbstractModel


def remove_string(to_edit):
    subject_to_remove = 'http://www.radlex.org/RID/#'
    return to_edit.replace(subject_to_remove, '')


def parse():
    owl_file = "Radlex3.14.owl"
    g = rdflib.Graph()
    g.load(owl_file)
    m = AbstractModel()
    for subject, predicate, obj in g:
        if "Preferred_name" in predicate:
            m.add_name(remove_string(str(subject)), remove_string(str(obj)))

        elif "Synonym" in predicate:
            m.add_syn(remove_string(str(subject)), remove_string(str(obj)))

        elif "Preferred_Name_for_Obsolete" in predicate:
            m.add_obsolete_name(remove_string(str(subject)), remove_string(str(obj)))

    filename = 'this.txt'
    m.save(filename)


if __name__ == '__main__':
    parse()
