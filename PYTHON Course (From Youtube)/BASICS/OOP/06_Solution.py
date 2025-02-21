# car_Count 

class Car:
    car_Count = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.car_Count += 1

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

ElCar("Tesla", "Model S", "85KWh")
Car("Tata", "punch")


print(Car.car_Count)