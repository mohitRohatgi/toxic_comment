import unittest
import os

from toxic_comment.definitions import ROOT_DIR
from toxic_comment.main.pre_processor.data_points_builder import DataPointsBuilder


class TestDataPointsBuilder(unittest.TestCase):
    def test_build_and_get_train_data_points(self):
        train_path = os.path.join(ROOT_DIR, "main/data/train.csv")
        test_path = os.path.join(ROOT_DIR,"main/data/test.csv")
        builder = DataPointsBuilder(",")
        data_points = builder.build_and_get_test_data_points(test_path)
        self.assertTrue(len(data_points.ids) > 0)

        data_points = builder.build_and_get_train_data_points(train_path)
        self.assertTrue(len(data_points.ids) > 0)
