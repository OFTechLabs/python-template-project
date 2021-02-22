from typing import List, Optional, Dict
import uvicorn
import os

from fastapi import FastAPI, Body
from pydantic import BaseModel
import mimetypes

import pickle

app = FastAPI(
    title="App deployment as a microservice",
    description="This project helps you to setup your Python application as a microservice, by hosting it"
                "in a Docker container, accessible through REST API.",
    version="0.1.0",
)

mimetypes.init()

MODEL_DIR = "app"
MODEL_NAME = "DecisionTreeClassifier"


class Flower(BaseModel):
    flower_names = ["setosa", "versicolor", "virginica"]
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def predict_flower_class(self, model) -> int:
        return model.predict([[self.sepal_length,
                               self.sepal_width,
                               self.petal_length,
                               self.petal_width]])[0]

    def predict_flower_name(self, model) -> str:
        return self.flower_names[self.predict_flower_class(model)]


class Prediction(BaseModel):
    predicted_class: int
    predicted_name: str


@app.post("/predict/", response_model=Prediction)
def predict_model(flower: Flower) -> Prediction:
    path = os.path.join(os.getcwd(), MODEL_DIR, MODEL_NAME + ".pickle")
    print(path)
    print("isfile", os.path.isfile(path))
    f_open = open(path, "rb")
    model = pickle.load(f_open)
    return Prediction(predicted_class=flower.predict_flower_class(model),
                      predicted_name=flower.predict_flower_name(model))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
