import os
import pickle

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


class Model(DecisionTreeClassifier):

    def __init__(self, model_dir: str, model_name: str, data_loader):
        super().__init__()
        self.model_dir = model_dir
        self.model_name = model_name
        self.data_loader = data_loader

    def load_iris_data(self):
        return self.data_loader()

    def save(self):
        with open(os.path.join(self.model_dir, self.model_name) + ".pickle", "wb") as file:
            pickle.dump(self, file, protocol=2)


model = Model(model_dir=os.path.dirname(__file__), model_name="DecisionTreeClassifier", data_loader=load_iris)

data = model.load_iris_data()
X = data.data
y = data.target
model.random_state = 0
model.min_samples_leaf = 3

model.fit(X, y)

model.save()

