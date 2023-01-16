class Pet():
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = int(age)

    def get_name(self):
        return self.name


    def get_species(self):
        return self.species

    def get_age(self): #returns the age of the pet
        return self.age

    def set_name(self, new_name: str):  #sets the name of the pet to the given value and returns the new name
        self.name = new_name
        return self.name

    def set_species(self, new_species: str):    # sets the species of the pet to the given value and returns the new
                                                # species
        self.species = new_species
        return self.species

    def set_age(self, new_age: int):
        self.age = new_age
        return self.age


pet = Pet("Fido", "Dog", 5)
print(pet.get_name())           # "Fido"
print(pet.get_species())        # "Dog"
print(pet.get_age())            # 5
print(pet.set_name("Buddy"))    # "Buddy"
print(pet.set_species("Cat"))   # "Cat"
print(pet.set_age(6))           # 6