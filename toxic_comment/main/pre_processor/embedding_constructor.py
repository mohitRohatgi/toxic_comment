import yaml
import numpy as np


class EmbeddingConstructor:
    def __init__(self):
        self.paths = self._get_paths()
        self.root_path = '../../'
        self.embed_path = self.paths['embed_path']
        self.train_path = self._get_abs_path(self.paths['train_path'])
        self.test_path = self._get_abs_path(self.paths['test_path'])
        self.word2Id_path = self._get_abs_path('word2Id_path')
        self.id2Word_path = self._get_abs_path('id2Word_path')
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
        if self._vocab_dicts_created():
            self._load_vocab_dicts()
        else:
            self._build_and_save_vocab()

        if self.embed_matrix_created():
            self._load_embed_matrix()
        else:
            self._build_and_save_embed_matrix()

    def _build_and_save_vocab(self):
        pass

    def _build_and_save_embed_matrix(self):
        self.embed_matrix = self._build_embed_matrix()
        return self._save_embed_matrix()
