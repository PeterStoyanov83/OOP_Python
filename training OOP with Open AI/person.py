'''Create a class called Person that has three instance variables: name, age, and gender.
The class should have a method called greet(), which returns a greeting in the form of a
string that includes the person's name.'''


class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person = Person("John", 30, "male")
greeting = person.greet()
print(greeting)
