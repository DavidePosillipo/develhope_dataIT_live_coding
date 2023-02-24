"""EX 2
(Usare l'ereditarietà)

For the purposes of these exercises, you are the director of IT at a zoo. The zoo contains several different kinds of animals,
 and for budget reasons, some of those animals have to be housed alongside other animals.

We will represent the animals as Python objects, with each species defined as a distinct class. 
All objects of a particular class will have the same species and number of legs, but the color will vary from one instance to another.

We’re going to assume that our zoo contains four different types of animals: sheep, wolves, snakes, and parrots.
(The zoo is going through some budgetary difficulties, so our animal collection is both small and unusual.) 
Create classes for each of these types, such that we can print each of them and get a report on their color, species, and number of legs."""


#------------------------------------------------------------------------------------


#creo la classe animal con l'attributo privatizzato'color'.
#uso property e setter per creare il meccanismo che mi permette di interagire in modo sicuro con 'color'.

class animal:
    def __init__(self,color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):

        if not isinstance(value,str):
            raise TypeError('Expected str')
        self._color = value     
    
#creo un metodo che mi restituisce il nome dell'oggetto come una stringa, mi servira' successivamente
    def get_object_name(self):
        globals_dict = globals()
        for name, value in globals_dict.items():
            if id(value) == id(self):
                return str(name)     

#creo le subclassi sheep,wolf,snake,parrot dove aggiungo 2 metodi che mi restituiscono la specie e il numero di gambe. 
class sheep(animal):
    def legs(self):
        return '4'

    def specie(self):
        return 'Sheep'  

class wolf(animal):
    def legs(self):
        return '4'

    def specie(self):
        return 'wolf'

        
class snake(animal):
    def legs(self):
        return '0'

    def specie(self):
        return 'snake'

class parrot(animal):
    def legs(self):
        return '2'

    def specie(self):
        return 'parrot'                           

#creo 9 animali diversi.

annabelle = sheep('bianca')
armanda = sheep('marrone')
dolly = sheep('blu_spaziale')

canepazzo = wolf('nero')
corrado = wolf('grigio')

jake = snake('verde')
piton = snake('nero')

pablo = parrot('magenta')
rossita = parrot ('scarlatto')

#creo una lista di tuple con tutte le informazioni che mi servono per creare il report.
animali_zoo = [annabelle,armanda,dolly,canepazzo,corrado,jake,piton,pablo,rossita]
report_data =[(animale.get_object_name(),animale.specie(),animale.legs(),animale.color) for animale in animali_zoo]


#creo una funzione che mi permetta di sistemare i dati contenuti nella lista di tuple in un modo graficamente ordinato.
def print_report(reportdata):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Nome','Specie','Legs','Colore')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10s %10s %10s' % row )

print_report(report_data)
