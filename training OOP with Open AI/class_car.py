class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def set_make(self, new_make):
        self.make = new_make
        return self.make

    def set_model(self, new_model):
        self.model = new_model
        return self.model

    def set_year(self, new_year):
        self.year = new_year
        return self.year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"



car = Car("Ford", "Mustang", 2020)
print(car.get_make())  # "Ford"
print(car.get_model())  # "Mustang"
print(car.get_year())  # 2020
car.set_make("Chevrolet")
print(car.get_make())  # "Chevrolet"
print(car)  # "2020 Chevrolet Mustang"

'''Create a class called Car that has three instance variables: make, model, and year.

The class should have the following methods:

__init__(self, make, model, year): This is the constructor for the class. It should initialize
the make, model, and year instance variables.
get_make(self): This method should return the make of the car
get_model(self): This method should return the model of the car
get_year(self): This method should return the year of the car
set_make(self, make): This method should set the make of the car
set_model(self, model): This method should set the model of the car
set_year(self, year): This method should set the year of the car
__str__(self): This method should return a string representation of the car in the following format: "year make model"'''
