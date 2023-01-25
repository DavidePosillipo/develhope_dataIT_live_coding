# 1. Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

str = 'Python'
for i in str:
    if i == 'o':
        continue
    print (i)


# 2. Usando la lista:
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

# scrivete un for loop che printi una riga come "BoJack Horseman is a horse voiced by Will Arnet." per ogni elemento della lista. 


for i in main_characters:
    print(f'{i[0]} is a {i[2]} voiced by {i[1]}')
