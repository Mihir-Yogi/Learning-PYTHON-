# isinstance ==> we can check the my_car object is Car class or ElCar class intance or not.

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
    
class ElCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_car = ElCar("Tesla", "Model S", "85KWh")

print(my_car.full_name())
print(isinstance(my_car, Car))
print(isinstance(my_car, ElCar))