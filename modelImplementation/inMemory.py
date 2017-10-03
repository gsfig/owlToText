import re
import json


# subject is key
class ModelinMemory:
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

    def from_file(self, file_path):
        with open(file_path) as file:
            data = json.load(file)

        for id in data:
            for tag in data[id]:
                for item in data[id][tag]:
                    self.add(str(id), str(item), tag)

    def check_exists(self, id):
        raise NotImplementedError("error message")



