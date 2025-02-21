
# fullName ==> also we can create a normal methods in the class but only __init__ name method through we can create constructor.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"

my_Car = Car("Tata", "Safari")
print(my_Car.fullName())