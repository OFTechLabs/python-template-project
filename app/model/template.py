class Car(object):
    def __init__(self, brand, mileage, owner=None):
        self.brand = brand
        self.owner = owner
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance


class CarFactory(object):
    def __init__(self, brand, capacity=2):
        self.capacity = capacity
        self.brand = brand

    def construct_cars(self):
        return [Car(self.brand, mileage=0) for _ in range(self.capacity)]


class CarManufacturer(object):
    def __init__(self, brand, factory_capacities):
        self.factories = [CarFactory(brand, capacity) for capacity in factory_capacities]

    def construct_cars(self):
        cars = []
        for factory in self.factories:
            cars.extend(factory.construct_cars())
        return cars
