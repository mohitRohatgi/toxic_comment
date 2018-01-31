import unittest
from toxic_comment.main.pre_processor.data_points_builder import DataPointsBuilder


class TestDataPointsBuilder(unittest.TestCase):
    def test_build_and_get_train_data_points(self):
        file_path = "/home/mrohatgi/PycharmProjects/toxicComment/toxic_comment/data/sample_submission.csv"
        builder = DataPointsBuilder(",")
        data_points = builder.build_and_get_test_data_points(file_path)
        self.assertTrue(len(data_points.ids) > 0)
