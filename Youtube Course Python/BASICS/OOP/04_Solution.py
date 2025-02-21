
# Encapsulation ==> __brand --> Private the veriable from doing double underscore on start that only access in class.
# getter method ==> for encapsulation we used a getter method to get brand name because it was privet using __brand.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def Get__brand(self):
        return self.__brand
    def fullName(self):
        return f"{self.__brand} {self.model}"

class ElCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_ElCar = ElCar("Tesla", "Model S", "85KWh")
# print(my_ElCar.brand)
# print(my_ElCar.__brand)
print(my_ElCar.Get__brand())
print(my_ElCar.model)
print(my_ElCar.battery_size)
print(my_ElCar.fullName())