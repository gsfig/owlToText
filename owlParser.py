import rdflib
from makeDB import MakeDB


def parse():
    owlFile = "Radlex3.14.owl"
    g = rdflib.Graph()
    g.load(owlFile)
    db = MakeDB()
    db.connect()
    db.createDB()
    i = 0
    for subject, predicate, obj in g:
        if "Preferred_name" in predicate:
            print(i + " pred " + str(subject) + " " + str(predicate) + " " + str(obj))
            db.add(str(subject), str(predicate), str(obj))
            db.connection.commit()
            i+=1

    print("end ")

    db.add("http://www.radlex.org/RID/#RID39426", "http://www.radlex.org/RID/#Preferred_name ", "muscle of iris")
    db.connection.commit()

    db.add("http://www.radlex.org/RID/#RID39426", "http://www.radlex.org/RID/#Preferred_name ", "muscle of iris")
    db.connection.commit()

    db.connection.close()


if __name__ == '__main__':
    parse()