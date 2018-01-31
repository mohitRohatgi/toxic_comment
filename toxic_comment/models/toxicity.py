class Toxicity(object):
    def __init__(self):
        self.id = []
        self.result = {}

    def add_result(self, id, toxic,severe_toxic,obscene,threat,insult,identity_hate):
        assert toxic <= 1.0
        assert severe_toxic <= 1.0
        assert obscene <= 1.0
        assert threat <= 1.0
        assert insult <= 1.0
        assert identity_hate <= 1.0
        self.id.append(id)
        self.result[id] = [toxic,severe_toxic,obscene,threat,insult,identity_hate]