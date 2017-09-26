import re
import json


# subject is key
class ModelMemory:
    data = dict()

    def add(self, subj, obj, tag):
        if subj in self.data:
            o = self.data.get(subj)
        else:
            o = dict()

        if tag not in o:
            o[tag] = list()

        # remove " and ' characters
        # TODO: use config.json array to remove chars
        s = re.sub('["]', '', obj)
        if s.startswith("'"):
            s = re.sub('[\']', '', s)

        o[tag].append(s)
        self.data[subj] = o

    def print(self, filename):
        f = open(filename, 'w')
        #f.write(str(self.data))
        json.dump(self.data, f)
        #pprint(self.data)
        f.close()

    def check_exists(self, id):
        raise NotImplementedError("error message")



