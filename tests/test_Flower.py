import unittest

from app.main import Flower

from sklearn.dummy import DummyClassifier


class TestFlower(unittest.TestCase):

    def setUp(self):
        self.sepal_length = 1.0
        self.sepal_width = 2.0
        self.petal_length = 3.0
        self.petal_width = 4.0
        self.flower = Flower(sepal_length=self.sepal_length,
                             sepal_width=self.sepal_width,
                             petal_length=self.petal_length,
                             petal_width=self.petal_width)
        self.flower_class = 1

    def test_init(self):
        self.assertEqual(self.flower.sepal_length, 1.0,
                         f"flower.sepal_length ({self.flower.sepal_length}) is not equal to 1.0")
        self.assertEqual(self.flower.sepal_width, 2.0,
                         f"flower.sepal_width ({self.flower.sepal_width}) is not equal to 2.0")
        self.assertEqual(self.flower.petal_length, 3.0,
                         f"flower.petal_length ({self.flower.petal_length}) is not equal to 3.0")
        self.assertEqual(self.flower.petal_width, 4.0,
                         f"flower.petal_width ({self.flower.petal_width}) is not equal to 4.0")

    def test_flower_names(self):
        self.assertListEqual(self.flower.flower_names, ["setosa", "versicolor", "virginica"],
                             f"flower_names ({self.flower.flower_names}) is not equal to "
                             f"[setosa, versicolor, virginica]")

    def test_predict_class(self):
        self.X = [[self.flower.sepal_length,
                   self.flower.sepal_width,
                   self.flower.petal_length,
                   self.flower.petal_width]]
        self.y = [self.flower_class]
        self.model = DummyClassifier()
        self.model.fit(self.X, self.y)
        self.predict = self.model.predict(self.X)

        self.assertEqual(self.predict, self.flower.predict_class(self.model),
                         f"model prediction ({self.predict}) is not equal to "
                         f"flower.predict_class ({self.flower.predict_class(self.model)}")

    def test_predict_name(self):
        self.X = [[self.flower.sepal_length,
                   self.flower.sepal_width,
                   self.flower.petal_length,
                   self.flower.petal_width]]
        self.y = [self.flower_class]
        self.model = DummyClassifier()
        self.model.fit(self.X, self.y)
        self.predict = self.flower.flower_names[self.model.predict(self.X)[0]]

        self.assertEqual(self.predict, self.flower.predict_name(self.model),
                         f"model prediction ({self.predict}) is not equal to "
                         f"flower.predict_class ({self.flower.predict_name(self.model)}")
