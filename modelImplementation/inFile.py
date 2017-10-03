import rdflib
import json


class ModelinFile:

    def print_to_json_file(self, data, filename):
        f = open(filename, 'w')
        json.dump(data, f)
        f.close()
        print("end print to file: " + str(filename))

    def printPredicates(self, owl_file):
        g = rdflib.Graph()
        g.load(owl_file)
        pred = list()
        i = 0
        for subject, predicate, obj in g:
            if predicate not in pred:
                pred.append(predicate)
                print(str(predicate))
                i += 1
        print("has " + str(i) + " predicates")

    def appendNamesForNer(self, file_read, file_to):
        filewrite = open(file_to, "w")
        with open(file_read, "r") as read:
            json_read = json.load(read)

        out = list()

        for rid in json_read:
            for tag in json_read[rid]:
                for item in json_read[rid][tag]:
                    out.append(item)
        out.sort()
        for s in out:
            filewrite.write(s)
            filewrite.write("\n")

        read.close()
        filewrite.close()

        print("end print to file: " + file_to)

