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
        self.split_distribution = (0.6, 0.8, 1.0)

    """
    This method adds a data point into the class.
    """
    def add(self, toxic_id, text, label:Label=None):
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
        train_end = round(self._get_train_split() * size)
        valid_end = round(self._get_valid_split() * size)
        self.train = self.ids[:train_end]
        self.valid = self.ids[train_end:valid_end]
        self.test = self.ids[valid_end:]
        return self

    def get_train_id2text(self):
        return self._get_sub_dict(self.train, self.id2text)

    def get_train_id2_label(self):
        return self._get_sub_dict(self.train, self.id2label)

    def get_valid_id2text(self):
        return self._get_sub_dict(self.valid, self.id2text)

    def get_valid_id2_label(self):
        return self._get_sub_dict(self.valid, self.id2label)

    def get_test_id2text(self):
        return self._get_sub_dict(self.test, self.id2text)

    def get_test_id2_label(self):
        return self._get_sub_dict(self.test, self.id2label)

    @staticmethod
    def _get_sub_dict(keys, dict):
        return {k: dict[k] for k in keys}

    def _get_train_split(self):
        return self.split_distribution[0]

    def _get_valid_split(self):
        return self._get_train_split() + self.split_distribution[1]
