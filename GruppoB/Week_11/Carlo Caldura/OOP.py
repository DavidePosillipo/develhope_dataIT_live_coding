class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour

def create_scoops():
    
    scoops = [Scoop('vanilla'), Scoop('chocolate'), Scoop('cream')]

    for scoop in scoops:
        print(scoop.flavour)

create_scoops()



class Animal:
    def __init__(self, species, number_of_legs, color):
        self. species = species
        self.number_of_legs = number_of_legs
        self.color = color

    def report_animal(self):
        print(f'This animal is a {self.species}, it has {self.number_of_legs} legs and is {self.color}.')
        
class Sheep(Animal):
    def __init__(self, color):
        super().__init__('sheep', 4, color)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__('wolf', 4, color)

class Snake(Animal):
    def __init__(self, color):
        super().__init__('snake', 0, color)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__('parrot', 2, color)

sheep = Sheep('white')                  
sheep.report_animal()

wolf = Wolf('grey')
wolf.report_animal()

snake = Snake('camouflage')
snake.report_animal()

parrot = Parrot('green')
parrot.report_animal()
