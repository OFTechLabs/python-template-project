from typing import List, Optional, Dict
import uvicorn
import os

from fastapi import FastAPI, Body
from pydantic import BaseModel
import mimetypes

from app.model.template import Car, CarFactory, CarManufacturer

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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
