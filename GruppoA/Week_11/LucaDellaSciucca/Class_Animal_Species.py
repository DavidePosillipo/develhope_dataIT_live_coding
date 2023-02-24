import random

class AnimalSpecies():
    def __init__(self, legs, species, color):
        self.legs = legs
        self.color = random.choice(color)
        self.species = species
    
    def report(self):
        return f"The {self.species} class has {self.legs} legs and is colored {self.color}"

class Sheep(AnimalSpecies):
    def __init__(self, color = ["Black", "White", "Brown", "Grey"], legs = 4, species = "Sheep"):
        super().__init__(legs, species, color)

class Wolf(AnimalSpecies):
    def __init__(self, color = ["Black", "White", "Brown", "Grey"], legs = 4, species = "Wolf"):
        super().__init__(legs, species, color)

class Snake(AnimalSpecies):
    def __init__(self, color = ["Black", "Yellow", "Red", "Green"], legs = 0, species = "Snake"):
        super().__init__(legs, species, color)

class Parrot(AnimalSpecies):
    def __init__(self, color = ["Yellow", "Red", "Green", "Blue"], legs = 2, species = "Parrot"):
        super().__init__(legs, species, color) 

Carol = Sheep()
print(Carol.report())


        


    