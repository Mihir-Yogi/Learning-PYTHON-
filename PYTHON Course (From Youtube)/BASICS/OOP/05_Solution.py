# Polymorphism ==> Polymorphism is reffers to same method tow class have but it hase diffrent functionality, Example:- fule_Type().

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def Get__brand(self):
        return self.__brand
    
    def fullName(self):
        return f"{self.__brand} {self.model}"

    def fule_Type(self):
        return "Desal Or Patrol !"
    
class ElCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fule_Type(self):
        return "Electric Charge !"

my_ElCar = ElCar("Tesla", "Model S", "85KWh")
# print(my_ElCar.brand)
# print(my_ElCar.__brand)
# print(my_ElCar.Get__brand())
# print(my_ElCar.model)
# print(my_ElCar.battery_size)
print(my_ElCar.fullName())
print(my_ElCar.fule_Type())

my_Car = Car("Tata", "punch")
print(my_Car.fullName())
print(my_Car.fule_Type())