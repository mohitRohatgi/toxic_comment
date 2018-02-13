import yaml
import numpy as np
import os
import pickle

from toxic_comment.definitions import ROOT_DIR

"""
embed path : embeddings file path. eg. glove vectors
embedding matrix path : path of the embedding matrix constructed
embedding: embedding loaded from embed_path file. e.g. glove vectors
embedding matrix: embedding matrix constructed from embeddings
"""


class EmbeddingConstructor:
    def __init__(self):
        self.paths = self._get_paths()
        self.root_path = ROOT_DIR
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
        self.embedding = None

    def construct(self):
        self._load_embedding()
        if self._vocab_dicts_and_matrix_created():
            self._load_vocab_and_matrix()
        else:
            self._build_and_save_vocab_and_matrix()
        return self

    def _get_paths(self):
        with open(self._get_abs_path("resources/paths.yml"), "r") as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                raise RuntimeWarning("glove vectors not found or wrong path provided.", exc)

    def _get_abs_path(self, path):
        return os.path.join(self.root_path, path)

    def _load_embedding(self):
        embedding = {}
        with open(self.embed_path) as embed_file:
            for line in embed_file:
                split_line = line.split()
                word = split_line[0]
                embed = np.array([float(val) for val in split_line[1:]])
                embedding[word] = embed

        return embedding

    def _vocab_dicts_and_matrix_created(self):
        return os.path.isfile(self.word2Id_path) and os.path.isfile(self.id2Word_path) and \
               os.path.isfile(self.embed_matrix_path)

    def _load_vocab_and_matrix(self):
        word2Id_file = open(self.word2Id_path, "r")
        self.word2Id = pickle.load(word2Id_file)
        word2Id_file.close()

        id2Word_file = open(self.id2Word_path, "r")
        self.id2Word = pickle.load(id2Word_file)
        id2Word_file.close()

        embedding_matrix_file = open(self.embed_matrix_path)
        self.embed_matrix = pickle.load(embedding_matrix_file)
        embedding_matrix_file.close()

        assert (self.word2Id is not None and self.id2Word is not None and self.embed_matrix is not  None)

    def _build_and_save_vocab_and_matrix(self):
        self.embed_matrix = np.zeros((len(self.embedding.keys()), len(self.embedding[self.embedding.keys()[0]])))
        for word_id, word in self.embedding.keys():
            self.word2Id[word] = word_id
            self.id2Word[word_id] = word
            self.embed_matrix[word_id] = self.embed_matrix[word]

        self._save_vocab_and_matrix()

    def _save_vocab_and_matrix(self):
        word2_id_file = open(self.word2Id_path, "w")
        pickle.dump(self.word2Id, word2_id_file)
        word2_id_file.close()

        id2_word_file = open(self.id2Word_path, "w")
        pickle.dump(self.id2Word, id2_word_file)
        id2_word_file.close()

        embedding_matrix_file = open(self.embed_matrix_path, "w")
        pickle.dump(self.embed_matrix, embedding_matrix_file)
        embedding_matrix_file.close()
