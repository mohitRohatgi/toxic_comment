from toxic_comment.models import toxicity

class Classifier(object):
    __metaclass__ = toxicity

    def train(self, train_file_path, delimiter):
        raise NotImplementedError("training api not implemented")

    def test(self, test_file_path) -> toxicity:
        raise NotImplementedError("testing api not implemented")
