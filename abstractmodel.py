from modelImplementation.inMemory import ModelMemory


class AbstractModel:
    m = ModelMemory()

    def add_name(self, subj, obj):
        self.m.add_name(subj, obj)

    def add_syn(self, subj, obj):
        self.m.add_syn(subj, obj)

    def check_exists(self, id):
        self.m.check_exists(id)

    def print(self):
        self.m.print()

    def save(self, filename):
        self.m.save(filename)