# inheritence ==> python can get multiple inheritence
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @property
    def model(self):
        return self.__model
    

class bettery:
    def bettery(self):
        return "This is Bettery!"

class Engine:
    def Engine(self):
        return "This is Engine!"

class ElCar(bettery, Engine, Car):
    pass


my_car = ElCar("Tesla", "Model S")
print(my_car.bettery())
print(my_car.Engine())