import re


# subject is key
class ModelinMemory:
    data = dict()

    def add(self, subj, obj, tag):
        """
        adds subject, object and predicate to data structure

        guarantees subjects are unique

        :param subj:
        :param obj:
        :param tag:
        :return: Nothing
        """
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


    def check_exists(self, id):
        raise NotImplementedError("error message")



