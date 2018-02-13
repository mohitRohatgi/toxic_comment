from toxic_comment.main.models.toxicity import Toxicity
from toxic_comment.main.models.data_points import DataPoints


class Classifier(object):

    """
    This api builds the model architecture.
    """
    def build_model_architecture(self):
        raise NotImplementedError("model architecture not implemented.")

    """
    Given training data, this method should train the model.
    """
    def train(self, train_data: DataPoints, epochs):
        raise NotImplementedError("training api not implemented")

    """
    Given validation data, this method should validate the model.
    """
    def valid(self, valid_data: DataPoints):
        raise NotImplementedError("validation api not implemented")

    """
    This api should plot the convergence graph.
    """
    def plot_convergence(self):
        raise NotImplementedError("convergence plotting not implemented")

    """
    This api should plot the roc curve.
    """
    def plot_roc(self):
        raise NotImplementedError("roc plotting api not implemented")

    """
    Given a test file path, computes the output and returns the object toxicity.
    """
    def test(self, test_data: DataPoints) -> Toxicity:
        raise NotImplementedError("testing api not implemented")
