

class InMemoryObject:
    def __init__(self):
        self.pref_name = None
        self.id = None
        self.synonyms = list()

    def __iter__(self):
        return self

    def __eq__(self, o) -> bool:
        return self.pref_name == o.pref_name and self.id == o.id

    def __hash__(self) -> int:
        return hash((self.pref_name, self.id))

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def __str__(self) -> str:
#        if self.id:
#            return "id: " + self.id
        if self.pref_name and self.synonyms:
            s = ''
            i = 1
            for l in self.synonyms:
                s += str(i) + " " + l + " "
                i += 1
            return "has all, " + "Name: " + self.pref_name + " Syn: " + s

        if self.synonyms and not self.pref_name:
            s = ''
            for l in self.synonyms:
                s+=l
            return "no name, number of l: " + str(self.synonyms.__len__()) + "l: " + s

        if not self.synonyms and self.pref_name:
            return "no syn " + "name " + self.pref_name

    def sting_output(self):
        if self.pref_name and self.synonyms:
            s = ''
            for l in self.synonyms:
                s += l + "\t"
            return self.pref_name + "\t" + s

        if self.synonyms and not self.pref_name:
            s = ''
            for l in self.synonyms:
                s+=l
            return "no name, number of l: " + str(self.synonyms.__len__()) + "l: " + s

        if not self.synonyms and self.pref_name:
            return "no syn " + "name " + self.pref_name

#    def print(self):
#        print("id: " + self.id + " " + self.pref_name + " " + self.synonyms)


# subject is key
class ModelMemory:
    data = dict()

    def add_syn(self, subj, obj):
        if subj in self.data:
            o = self.data.get(subj)
        else:
            o = InMemoryObject()
            o.id = subj
            self.data[subj] = o
        o.synonyms.append(obj)
        #print("s: " + subj)


    def add_name(self, subj, obj):
        if subj in self.data:
            o = self.data.get(subj)
        else:
            o = InMemoryObject()
            o.id = subj
            self.data[subj] = o
        o.synonyms.append(obj)
        o.pref_name = obj
        #print("s: " + subj + " name: " + o.pref_name)

    def print(self):
        #print("printing everything: " + str(self.data.__len__()))
        for k, v in self.data.items():
            print(k)
            print(v)

    def save(self, filename):
        headers = ['RID', 'prefered_name', 'Synonyms']
        f = open(filename, 'w')
        f.write('\t'.join(headers) + '\n')
        for k, v in self.data.items():
            print(k)
            f.write(k)
            f.write('\t')
            #print(v, file=filename)

            f.writelines(v.sting_output())

            f.write('\n')
        f.close()



    # no need. dictionary does update with or without existing (key,value) pair.
    def check_exists(self, id):
        raise NotImplementedError("error message")



