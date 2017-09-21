

class InMemoryObject:
    def __init__(self):
        self.pref_name = None
        self.obsolete_name = None
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

        if self.obsolete_name and self.synonyms:
            s = ''
            for l in self.synonyms:
                s += l + "\t"
            return self.obsolete_name + "\t" + s

        if not self.synonyms and self.obsolete_name:
            self.synonyms.append('')
            return self.obsolete_name + "\t" + ''

        if not self.synonyms and self.pref_name:
            self.synonyms.append('')
            return self.pref_name + "\t" + ''

        if self.synonyms and not self.pref_name and not self.obsolete_name:
            s = ''
            for l in self.synonyms:
                s+=l
            return self.id + "\t" + s

        if self.synonyms and not self.pref_name:
            s = ''
            for l in self.synonyms:
                s+=l
            print("ERROR: no name, number of l: "+ str(self.synonyms.__len__()) + "l: " + s)
            return "no name, number of l: " + str(self.synonyms.__len__()) + "l: " + s

    def is_obsolete(self):
        if self.obsolete_name and not self.pref_name:
            return True
        elif self.obsolete_name and self.pref_name:
            return True
        elif not self.obsolete_name and not self.pref_name:
            return False # but outputs RID as pref_name
        return False


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
        o.pref_name = obj
        #print("s: " + subj + " name: " + o.pref_name)

    def add_obsolete_name(self, subj, obj):
        if subj in self.data:
            o = self.data.get(subj)
        else:
            o = InMemoryObject()
            o.id = subj
            self.data[subj] = o
        o.obsolete_name = obj

    def print(self):
        #print("printing everything: " + str(self.data.__len__()))
        for k, v in self.data.items():
            print(k)
            print(v)

    def save(self, filename):
        headers = ['RID', 'prefered_name', 'Synonyms']
        headersobs = ['RID', 'obsolete_name', 'Synonyms']
        f = open(filename, 'w')
        obs = open("obsolete.txt", 'w')
        f.write('\t'.join(headers) + '\n')
        obs.write('\t'.join(headersobs) + '\n')
        for k, v in self.data.items():
            if v.is_obsolete():
                obs.write(k)
                obs.write('\t')
                obs.writelines(v.sting_output())
                obs.write('\n')
            else:
                f.write(k)
                f.write('\t')
                f.writelines(v.sting_output())
                f.write('\n')
        f.close()
        obs.close()

    def check_exists(self, id):
        raise NotImplementedError("error message")



