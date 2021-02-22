import unittest
import os
import pickle

from app.main import Flower
from app.main import Prediction
from app.main import predict_model

from sklearn.tree import DecisionTreeClassifier


class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_pickle_model(self):
        self.file_path = os.path.dirname(__file__)
        self.path = os.path.join(self.file_path, "..", "app", "model", "DecisionTreeClassifier.pickle")
        self.assertTrue(os.path.exists(self.path), f"the path ({self.path}) does not exist")
        self.assertTrue(os.path.isfile(self.path), f"the path ({self.path}) is not a file")
        self.f_open = open(self.path, "rb")
        self.model = pickle.load(self.f_open)
        self.assertIsInstance(self.model, DecisionTreeClassifier, "the model is of a different type than DecisionTreeClassifier")

    def test_Flower(self):
        self.flower = Flower(sepal_length=1.0, sepal_width=2.0, petal_length=3.0, petal_width=4.0)

        self.assertEqual(self.flower.sepal_length, 1.0)
        self.assertEqual(self.flower.sepal_width, 2.0)
        self.assertEqual(self.flower.petal_length, 3.0)
        self.assertEqual(self.flower.petal_width, 4.0)

        self.assertEqual(self.flower.flower_names, ["setosa", "versicolor", "virginica"])

    def test_model(self):
        self.flower = Flower(sepal_length=1.0, sepal_width=2.0, petal_length=3.0, petal_width=4.0)

        self.prediction = predict_model(self.flower)
        self.assertEqual(self.prediction.predicted_class, 2, "the prediction has a different predicted class than expected")
        self.assertEqual(self.prediction.predicted_name, "virginica", "the prediction has a different predicted name than expected")



