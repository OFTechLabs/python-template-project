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


class PredictionModel(object):
    def __init__(self, model, data_loader):
        self.model = model
        self.X = None
        self.y = None
        self.data_loader = data_loader
        self.feature_names = None
        self.target_names = None

    def get_data(self):
        """
        """
        data = self.data_loader()
        self.X = data.data
        self.y = data.target
        self.feature_names = data.feature_names
        self.target_names = data.target_names


    def fit(self, X_train, y_train):
        """
        """
        self.model.fit(X_train, y_train)
        return

    def predict(self, X):
        """
        """
        return self.target_names[self.model.predict(X)[0]]
