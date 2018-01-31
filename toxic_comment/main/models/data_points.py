from .label import Label
import numpy as np


class DataPoints(object):
    def __init__(self):
        self.ids = []
        self.id2text = {}
        self.id2label = {}
        self.train = None
        self.test = None
        self.valid = None

    """
    This method adds a data point into the class.
    """
    def add(self, toxic_id, text, label:Label):
        self.ids.append(toxic_id)
        self.id2text[toxic_id] = text
        self.id2label[toxic_id] = label
        return self

    """
    This method would split the data points into train, test and valid sets.
    Split is 60, 20, 20 respectively.
    """
    def split(self):
        self.ids = np.array(self.ids)
        np.random.shuffle(self.ids)
        size = len(self.ids)
        train_end = round(0.6 * size)
        valid_end = round(0.8 * size)
        self.train = self.ids[:train_end]
        self.valid = self.ids[train_end:valid_end]
        self.test = self.ids[valid_end:]
        return self
