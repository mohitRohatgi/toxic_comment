class Toxicity(object):
    def __init__(self, delimiter):
        self.ids = []
        self.result = {}
        self.delimiter = delimiter

    def add_result(self, id, toxic,severe_toxic,obscene,threat,insult,identity_hate):
        assert toxic <= 1.0
        assert severe_toxic <= 1.0
        assert obscene <= 1.0
        assert threat <= 1.0
        assert insult <= 1.0
        assert identity_hate <= 1.0
        self.ids.append(id)
        self.result[id] = [toxic,severe_toxic,obscene,threat,insult,identity_hate]

    def __str__(self):
        output = ""
        for id in self.ids:
            output += id + self.delimiter + self._get_concatenated(id) + "\n"
        return output

    def _get_concatenated(self, id):
        output = self.result[id].pop(0)
        while len(self.result[id]) > 0:
            output += self.delimiter + self.result[id].pop(0)
