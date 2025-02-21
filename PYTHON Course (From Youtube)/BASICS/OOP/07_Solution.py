# @staticmethod ==> it can create a static method. 

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
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
class ElCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fule_Type(self):
        return "Electric Charge !"

ElCar("Tesla", "Model S", "85KWh")
my_car = Car("Tata", "punch")

print(my_car.general_description())
print(Car.general_description())

