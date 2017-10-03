import rdflib
import json


class ModeltoFile:

    def print_to_file(self, data, filename):
        f = open(filename, 'w')
        #f.write(str(self.data))
        json.dump(data, f)
        #pprint(self.data)
        f.close()
        print("end printing to file: " + str(filename))

    def printPredicates(self):
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
                i += 1
        print("has " + str(i) + " predicates")

    def appendNamesForNer(self):
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
                    # out.append(item + " " + rid + " " +tag)
                    out.append(item)

        out.sort()
        for s in out:
            filewrite.write(s)
            filewrite.write("\n")

        data_file.close()
        read.close()
        filewrite.close()