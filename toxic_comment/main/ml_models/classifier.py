from toxic_comment.main.models import toxicity


class Classifier(object):

    """
    Given a training file path and delimiter, this method should train the model.
    Assumption is only one delimiter is used for separation of data
    """
    def train(self, train_file_path, delimiter):
        raise NotImplementedError("training api not implemented")

    """
    Given a test file path, compute the output and reeturn the object toxicity.
    """
    def test(self, test_file_path) -> toxicity:
        raise NotImplementedError("testing api not implemented")
