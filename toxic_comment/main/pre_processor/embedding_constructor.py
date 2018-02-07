import yaml
import numpy as np
from os.path import isfile
import pickle

"""
embed path : embeddings file path. eg. glove vectors
embedding matrix path : path of the embedding matrix constructed
embedding: embedding loaded from embed_path file. e.g. glove vectors
embedding matrix: embedding matrix constructed from embeddings
"""


class EmbeddingConstructor:
    def __init__(self):
        self.paths = self._get_paths()
        self.root_path = '../../'
        self.embed_path = self.paths['embed_path']
        self.train_path = self._get_abs_path(self.paths['train_path'])
        self.test_path = self._get_abs_path(self.paths['test_path'])
        self.word2Id_path = self._get_abs_path(self.paths['word2Id_path'])
        self.id2Word_path = self._get_abs_path(self.paths['id2Word_path'])
        self.embed_matrix_path = self._get_abs_path(self.paths['embed_matrix_path'])
        self.word2Id = None
        self.id2Word = None
        self.embed_matrix = None
        self.unknown = 'unk'
        self._load_vocab_dicts_and_embed_matrix()
        self.embedding = self._load_embedding()

    def _get_paths(self):
        with open(self._get_abs_path("resources/paths.yml"), "r") as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                raise RuntimeWarning("glove vectors not found or wrong path provided.", exc)

    def _get_abs_path(self, path):
        return self.root_path + path

    def _load_embedding(self):
        embedding = {}
        with open(self.embed_path) as embed_file:
            for line in embed_file:
                split_line = line.split()
                word = split_line[0]
                embed = np.array([float(val) for val in split_line[1:]])
                embedding[word] = embed

        return embedding

    def _load_vocab_dicts_and_embed_matrix(self):
        if self._vocab_dicts_and_matrix_created():
            self._load_vocab_and_matrix()
        else:
            self._build_and_save_vocab_and_matrix()

    def _build_and_save_vocab(self):
        pass

    def _vocab_dicts_and_matrix_created(self):
        return isfile(self.word2Id_path) and isfile(self.id2Word_path) and isfile(self.embed_matrix_path)

    def _load_vocab_and_matrix(self):
        self.word2Id = pickle.load(self.word2Id_path)
        self.id2Word = pickle.load(self.id2Word_path)
        self.embed_matrix = pickle.load(self.embed_matrix_path)
        assert (self.word2Id is not None and self.id2Word is not None and self.embed_matrix is not  None)

    def _build_and_save_vocab_and_matrix(self):
        pass
