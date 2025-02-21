# Inheritence ==> ElCar(Car) --> ElCar inheriting the Car class like Car class is a parent of ElCar class 
# super() ==> super keyword can access directly the parent methods 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"

class ElCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_ElCar = ElCar("Tesla", "Model S", "85KWh")
print(my_ElCar.brand)
print(my_ElCar.model)
print(my_ElCar.battery_size)
print(my_ElCar.fullName())