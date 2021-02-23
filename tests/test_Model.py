import unittest
import os
import pickle

import numpy as np
from sklearn.datasets import load_iris

from app.model.Model import Model


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model_dir = os.path.dirname(__file__)
        self.model_name = "TestDecisionTreeClassifier"
        self.data_loader = load_iris
        self.model = Model(model_dir=self.model_dir, model_name=self.model_name, data_loader=load_iris)

    def test_init(self):
        self.assertEqual(self.model_dir, self.model.model_dir)
        self.assertEqual(self.model_name, self.model.model_name)
        self.assertEqual(self.data_loader, self.model.data_loader)

    def test_load_data(self):
        self.data = self.model.load_data()
        np.testing.assert_array_almost_equal(self.data.data, load_iris().data)

    def test_save(self):
        self.model.save()
        self.saved_model = pickle.load(open(os.path.join(self.model_dir, self.model_name) + ".pickle", "rb"))
        self.assertIsInstance(self.saved_model, Model)
        self.assertEqual(self.model.model_dir, self.saved_model.model_dir)
        self.assertEqual(self.model.model_name, self.saved_model.model_name)
        self.assertEqual(self.model.data_loader, self.saved_model.data_loader)
        self.assertEqual(self.model.random_state, self.saved_model.random_state)
        self.assertEqual(self.model.criterion, self.saved_model.criterion)



