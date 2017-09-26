from modelImplementation.inMemory import ModelMemory


class AbstractModel:
    m = ModelMemory()

    def add(self, subj, obj, tag):
        self.m.add(subj, obj, tag)

    def check_exists(self, id):
        self.m.check_exists(id)

    def print(self, filename):
        self.m.print(filename)
