from toxic_comment.main.models.toxicity import Toxicity
from toxic_comment.main.models.data_points import DataPoints


class Classifier(object):

    """
    Given a training file path and delimiter, this method should train the model.
    Assumption is only one delimiter is used for separation of data.
    """
    def train(self, train_data: DataPoints):
        raise NotImplementedError("training api not implemented")

    """
    Given a test file path, computes the output and returns the object toxicity.
    """
    def test(self, test_data: DataPoints) -> Toxicity:
        raise NotImplementedError("testing api not implemented")
