# EX 1
'''
In this exercise, you'll define a class, Scoop, that represents a single scoop of ice cream.
Each scoop should have a single attribute, flavor, a string that you can initialize when you create the instance of Scoop.
Once your class is created, write a function (create_scoops) that creates three instances of the Scoop class, each of which has a different flavor.
Put these three instances into a list called scoops. Finally, iterate over your scoops list, printing the flavor.
'''

class Scoop:

    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(flavor_1, flavor_2, flavor_3):
    return [Scoop(flavor_1), Scoop(flavor_2), Scoop(flavor_3)]

scoops = create_scoops('chocolate', 'coffee', 'cream')

print("Scoops' flavor:")
for scoop in scoops:
    print(scoop.flavor)

# EX 2
'''
For the purposes of these exercises, you are the director of IT at a zoo.
The zoo contains several different kinds of animals, and for budget reasons, some of those animals have to be housed alongside other animals.
We will represent the animals as Python objects, with each species defined as a distinct class.
All objects of a particular class will have the same species and number of legs, but the color will vary from one instance to another.
We're going to assume that our zoo contains four different types of animals: sheep, wolves, snakes, and parrots.
(The zoo is going through some budgetary difficulties, so our animal collection is both small and unusual.)
Create classes for each of these types, such that we can print each of them and get a report on their color, species, and number of legs.
'''

class Animal:
    
    num_of_legs = 4
    
    def __init__(self, color):
        self.color = color
        
class Sheep(Animal):

    def __init__(self, color):
        super().__init__(color)
    
class Wolf(Animal):

    def __init__(self, color):
        super().__init__(color)

class Snake(Animal):
    
    num_of_legs = 0
    
class Parrot(Animal):
    
    num_of_legs = 2
    
white_sheep = Sheep('white')
black_sheep = Sheep('black')

gray_wolf = Wolf('gray')
brown_wolf = Wolf('brown')

green_snake = Snake('green')
yellow_snake = Snake('yellow')

rainbow_parrot = Parrot('rainbow')
brown_parrot = Parrot('brown')

print("\nAnimals' attributes:")
for animal, animal_inst in [('white_sheep', white_sheep), ('black_sheep', black_sheep), ('gray_wolf', gray_wolf), ('brown_wolf', brown_wolf), ('green_snake', green_snake), ('yellow_snake', yellow_snake), ('rainbow_parrot', rainbow_parrot), ('brown_parrot', brown_parrot)]:
    print(f"{animal} color: {animal_inst.color}, number of legs: {animal_inst.num_of_legs}")

# EX 3
'''
In the previous exercise, we created a Scoop class that represents one scoop of ice cream.
If we’re really going to model the real world, though, we should have another object into which we can put the scoops.
I thus want you to create a Bowl class, representing a bowl into which we can put our ice cream; for example:
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
'''

class Bowl():

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoops):
            self.scoops.extend(scoops)

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)

print("\nScoops in the bowl:")
for scoop in b.scoops:
    print(scoop.flavor)