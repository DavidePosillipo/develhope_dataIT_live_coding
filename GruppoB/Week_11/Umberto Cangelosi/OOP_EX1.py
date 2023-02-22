"""EX 1
In this exercise, you’ll define a class, Scoop, that represents a single scoop of ice cream.
Each scoop should have a single attribute, flavor, a string that you can initialize when you 
create the instance of Scoop. Once your class is created, write a function (create_scoops) that 
creates three instances of the Scoop class, each of which has a different flavor. 
Put these three instances into a list called scoops. Finally, iterate over your scoops list, 
printing the flavor.
"""
class Scoop:
    def __init__(self, flavour):
        self.set_flavour(flavour)

    def get_flavour(self):
        return self._flavour

    def set_flavour(self, string):
        if not isinstance(string,str):
            raise TypeError('Expected a string')
        self._flavour=string   
        
def create_scoop(gusto1,gusto2,gusto3):
    gusto1= Scoop(gusto1)
    gusto2= Scoop(gusto2)
    gusto3= Scoop(gusto3)
    return gusto1,gusto2,gusto3


scoops = create_scoop('nocciola','caffe','gelsi') 

for elemento in scoops: 
    print(elemento.get_flavour())
   
