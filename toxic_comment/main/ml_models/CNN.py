from toxic_comment.main.config.config import Config
from toxic_comment.main.models.data_points import DataPoints
from toxic_comment.main.models.toxicity import Toxicity
from .classifier import Classifier
import tensorflow as tf


class CNNClassifier(Classifier):
    def build_model_architecture(self, config: Config):
        self.config = config

    def plot_convergence(self):
        pass

    def train(self, train_data: DataPoints, epochs):
        pass

    def plot_roc(self):
        pass

    def valid(self, valid_data: DataPoints):
        pass

    def test(self, test_data: DataPoints) -> Toxicity:
        pass

    def _add_placeholders(self):
        self.input_placeholder = tf.placeholder(tf.int32, shape=(self.config.batch_size, self.config.max_seq_length))
        self.labels_placeholder = tf.placeholder(tf.int32, shape=(self.config.batch_size, self.config.num_classes))
        self.dropout_placeholder = tf.placeholder(tf.float32, shape=())
        self.embedding_placeholder = tf.get_variable("embeddings", shape=(self.config.vocab_size, self.config.embedding_size),
                                    initializer=tf.constant(0.0, shape=(self.config.vocab_size, self.config.embedding_size)))

    def _add_model(self):
        pass

    def _add_embedding_layer(self):
        with tf.variable_scope("embedding_layer", reuse=True):
            self.embedding = tf.get_variable("embedding", shape=(self.config.vocab_size, self.config.embedding_size),
                          initializer=tf.constant(0.0, shape=(self.config.vocab_size, self.config.embedding_size)),
                          name="embedding")
            batch_input = tf.nn.embedding_lookup(self.embedding, self.input_placeholder)
            batch_input_expanded = tf.expand_dims(batch_input, axis=-1)
        return batch_input_expanded

    def _add_conv_layer(self, input, position=1):
        with tf.variable_scope("conv_layer" + str(position)):
            W = tf

    def _projection(self):
        pass

    def _loss_op(self):
        pass

    def _run_epoch(self):
        pass

    def _test_model(self):
        pass
