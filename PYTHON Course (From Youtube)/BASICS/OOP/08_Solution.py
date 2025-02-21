# @property ==> it creates method that we want to not modify the value of specific variable then we can use the @property Decorator.

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
    def pr1(self):
        return self.__model
    
class ElCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fule_Type(self):
        return "Electric Charge !"



my_car = Car("Tata", "punch")

my_car.__model =  "ABC"

print(my_car.full_name())