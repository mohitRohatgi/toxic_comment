class Label(object):
    def __init__(self, toxic, severe_toxic, obscene, threat, insult, identity_hate):
        self.toxic = toxic
        self.severe_toxic = severe_toxic
        self.obscene = obscene
        self.threat = threat
        self.insult = insult
        self.identity_hate = identity_hate

    def __str__(self):
        return "{ " + "\n\t" + \
               "toxic: " + str(self.toxic) + "," + "\n\t" + \
               "severe_toxic: " + str(self.severe_toxic) + "," + "\n\t" + \
               "obscene: " + str(self.obscene) + "," + "\n\t" + \
               "threat: " + str(self.threat) + "," + "\n\t" + \
               "insult: " + str(self.insult) + "," + "\n\t" + \
               "identity_hate: " + str(self.identity_hate) + \
               "\n}"
