from app.model.template import Car, CarFactory, CarManufacturer

def test_car():
  car = Car(brand="Renault", mileage=123_456)
  distance = 544
  car.drive(distance)
  assert car.mileage == 124_000

def test_car_factory():
  car_factory = CarFactory(brand="Renault", capacity=3)
  cars = car_factory.construct_cars()
  assert len(cars) == 3

def test_car_manufacturer():
  car_manufacturer = CarManufacturer(brand="Renault", factory_capacities=[2, 3])
  cars = car_manufacturer.construct_cars()
  assert (len(car_manufacturer.factories) == 2) and (len(cars) == 5)
