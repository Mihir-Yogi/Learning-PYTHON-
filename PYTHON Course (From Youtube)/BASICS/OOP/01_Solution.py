# class ==> we can create a class using class keyword in python because python is a object oriented lenguage
# __init__ ==> __init__ double underscore init method reffers to be constructor of the class that method run first in the class. 
# self ==> self keyword is a connection between methods and class without self method variable and method can not be connected with class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_Car = Car("Tata", "Safari")
print(my_Car.brand)
print(my_Car.model)