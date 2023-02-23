"""import random

class Scoop():
    
    def __init__(self, num_flavors = 1, flavor = ["chocolate", 'cream', "lemon", "Cookie"]):
        self.flavor = random.choices(flavor, k = num_flavors)
    
    def __str__(self):                                 # or  def __depr__() ??
        return str(self.flavor)
    
    def get_flavor(self):
        return self.flavor
     
    def n_scoops(self, n = 3):
        scoops_ls = []
        for i in range(n):
            scoops_ls.append(Scoop())
        return scoops_ls

ice_cream1 = Scoop(3)
scoop_ls = Scoop.n_scoops(object, 6)
print(", ".join(str(scoop.flavor) for scoop in scoop_ls))
print(ice_cream1.flavor)
"""
    

import random
            
class Scoop:
    available = ["cioccolato", "crema", "panna", "pistacchio", "stracciatella", "amarena", "nocciola", "fior di latte", "limone", "frutti di bosco"]
    def __init__(self, flavor):
        self.flavor = flavor

    @classmethod
    def create_scoops_random(cls):
        icecream = []
        for n in range(3):
            icecream.append(Scoop(random.choice(Scoop.available)))
        return icecream
    
    @classmethod
    def choose_scoops(cls): 
        size = int(input("How many scoops for your icecream?: "))
        while type(size) != int:
            size = input("choose the NUMBER of scoops")
        
        menu = list(enumerate(Scoop.available))
        icecream = []
        n = 0

        while n < size:
            n += 1
            scoop = input(f"Available FLAVORS {menu}\n Type the flavor or the corrisponding number to have it in the icecream: ")
            for i in range(0, len(menu)):
                if int(scoop) == menu[i][0] or scoop == menu[i][1]:
                    icecream.append(Scoop(menu[i][1]))
            if len(icecream) != n:
                print("NOT available")
                n -= 1
        return icecream  

random_icecream = Scoop.create_scoops_random()
for scoop in random_icecream:
    print(scoop.flavor)

icecream = Scoop.choose_scoops()
for scoop in icecream:
    print(scoop.flavor)
            









 
        
