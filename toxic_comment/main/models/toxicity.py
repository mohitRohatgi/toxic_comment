class Toxicity(object):
    def __init__(self, delimiter):
        self.ids = []
        self.result = {}
        self.delimiter = delimiter

    def add_result(self, toxic_id, toxic,severe_toxic,obscene,threat,insult,identity_hate):
        assert toxic <= 1.0
        assert severe_toxic <= 1.0
        assert obscene <= 1.0
        assert threat <= 1.0
        assert insult <= 1.0
        assert identity_hate <= 1.0
        self.ids.append(toxic_id)
        self.result[toxic_id] = [toxic,severe_toxic,obscene,threat,insult,identity_hate]

    def __str__(self):
        output = ""
        for toxic_id in self.ids:
            output += toxic_id + self.delimiter + self._get_concatenated(toxic_id) + "\n"
        return output

    def _get_concatenated(self, toxic_id):
        output = self.result[toxic_id].pop(0)
        while len(self.result[toxic_id]) > 0:
            output += self.delimiter + self.result[toxic_id].pop(0)
        return output
