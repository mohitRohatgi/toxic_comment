import yaml
import numpy as np


class EmbeddingConstructor:
    def __init__(self):
        self.paths = self._get_paths()
        self.embed_path = self.paths['embed_path']
        self.train_path = self.paths['train_path']
        self.test_path = self.paths['test_path']
        self.embed = None
        self.unknown = 'unk'

    def load_embedding_and_get_glove(self):
        self.embed = self._load_embed()
        assert (self.embed is not None)
        return self.embed

    @staticmethod
    def _get_paths():
        with open("../../resources/paths.yml", "r") as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                raise RuntimeWarning("glove vectors not found or wrong path provided.", exc)

    def _load_embed(self):
        model = {}
        with open(self.embed_path) as embed_file:
            for line in embed_file:
                split_line = line.split()
                word = split_line[0]
                embedding = np.array([float(val) for val in split_line[1:]])
                model[word] = embedding
        return model

    def build_vocab(self):
        pass
