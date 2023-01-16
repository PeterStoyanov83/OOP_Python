"""Create a class called Person that has the following attributes:

name (str)
age (int)
gender (str)
The class should have the following methods:

get_name() which returns the name of the person
get_age() which returns the age of the person
get_gender() which returns the gender of the person
set_name(new_name: str) which sets the name of the person to the given value and returns the new name
set_age(new_age: int) which sets the age of the person to the given value and returns the new age
set_gender(new_gender: str) which sets the gender of the person to the given value and returns the new gender
__str__() which returns a string representation of the person in the format: "{name} is a {age} year old {gender}"
Create an instance of the class and test the methods by calling them and printing the returned values."""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender


    def set_name(self, new_name: str):
        self.name = new_name
        return self.name

    def set_age(self, new_age: int):
        self.age = new_age
        return self.age

    def set_gender(self, new_gender: str):
        self.gender = new_gender
        return self.gender


    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.gender}"


