from typing import List, Optional, Dict
import uvicorn
import os

from fastapi import FastAPI, Body
from pydantic import BaseModel
import mimetypes

from app.model.template import Car, CarFactory, CarManufacturer
from app.model.template import PredictionModel
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

app = FastAPI(
    title="App deployment as a microservice",
    description="This project helps you to setup your Python application as a microservice, by hosting it"
                "in a Docker container, accessible through REST API.",
    version="0.1.0",
)


mimetypes.init()


class ResponseCar(BaseModel):
    brand: str
    mileage: int
    owner: Optional[str]

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/cars/", response_model=List[ResponseCar])
def get_cars() -> List[ResponseCar]:
    """
    Get a list of all cars in the 'database'
    """
    car1 = Car(brand="Ford", mileage=100_000)
    car2 = Car(brand="Renault", mileage=265_000)
    cars = [car1, car2]

    response_cars = [ResponseCar(brand=car.brand, mileage=car.mileage) for car in cars]

    return response_cars


@app.post("/construct/", response_model=List[ResponseCar])
def build_cars(
        manufacturers: List[Dict[str, List[int]]] = Body(
            default=[{"Renault": [5]}],
            description="A list of manufacturers (as dictionaries) mapping the brand to a list of factory capacities"
        )
) -> List[ResponseCar]:
    """
    Construct a number of cars
    """
    car_manufacturers = [CarManufacturer(brand, capacities) for brand, capacities in manufacturers.items()]
    cars = []
    for car_manufacturer in car_manufacturers:
        cars.extend(car_manufacturer.construct_cars())

    response_cars = [ResponseCar(brand=car.brand, mileage=car.mileage) for car in cars]

    return response_cars

@app.post("/xcars/", response_model=List[ResponseCar])
def get_xcars(user: User, x: int = Body(default=2)) -> List[ResponseCar]:
    """
    Get a list of x cars of Ford
    """
    car = Car(brand="Ford", mileage=100_000)
    cars = [car]*x
    print(user.username, user.full_name)

    response_cars = [ResponseCar(brand=car.brand, mileage=car.mileage) for car in cars]

    return response_cars


@app.post("/predict/", response_model=str)
def predict_model(flower: Flower = Body(...)) -> str:
        est = PredictionModel(model=DecisionTreeClassifier(min_samples_leaf=3, random_state=0), data_loader=load_iris)
        est.get_data()
        est.fit(est.X, est.y)
        return est.predict([[flower.sepal_length, flower.sepal_width, flower.petal_length, flower.petal_width]])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
