class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = int(odometer_reading)


class ElectricCar(Car):
    def __init__(self, battery_size, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def drive(self, miles):
        self.odometer_reading -= miles
        return self.odometer_reading

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_odometer_reading(self):
        return self.odometer_reading

    def set_make(self, new_make):
        self.make = new_make
        return self.make

    def set_model(self, new_model):
        self.model = new_model
        return self.model

    def set_year(self, new_year):
        self.year = new_year
        return self.year

    def set_odometer_reading(self, new_reading):
        self.odometer_reading = new_reading
        return self.odometer_reading

    def drive(self, miles):
        self.odometer_reading += miles

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# car = Car("Ford", "Mustang", 2020)
# print(car.get_make())  # "Ford"
# print(car.get_model())  # "Mustang"
# print(car.get_year())  # 2020
# car.set_make("Chevrolet")
# print(car.get_make())  # "Chevrolet"
# print(car)  # "2020 Chevrolet Mustang"


car = Car("Toyota", "Prius", 2020, 25000)
print(car.get_make()) # "Toyota"
print(car.get_model()) # "Prius"
print(car.get_year()) # 2020
print(car.get_odometer_reading()) # 25000
car.drive(100)
print(car.get_odometer_reading()) # 25100
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
