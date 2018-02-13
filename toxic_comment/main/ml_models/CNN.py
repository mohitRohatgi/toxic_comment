from toxic_comment.main.config.config import Config
from toxic_comment.main.models.data_points import DataPoints
from toxic_comment.main.models.toxicity import Toxicity
from .classifier import Classifier


class CNNClassifier(Classifier):
    def build_model_architecture(self, config: Config):
        pass

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
        pass

    def _add_model(self):
        pass

    def _projection(self):
        pass

    def _loss_op(self):
        pass

    def _run_epoch(self):
        pass

    def _test_model(self):
        pass
