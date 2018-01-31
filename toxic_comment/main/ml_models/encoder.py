from .classifier import Classifier
from toxic_comment.main.models.data_points import DataPoints
from toxic_comment.main.models.toxicity import Toxicity


class Encoder(Classifier):

    def __init__(self):
        self.model = self.Model()

    # TODO: implement encoder model
    def train(self, train_data: DataPoints):
        pass

    def test(self, test_data: DataPoints) -> Toxicity:
        pass

    class Model:
        pass
