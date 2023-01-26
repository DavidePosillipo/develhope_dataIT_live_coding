# Week 7 - Exercise 2 - Carlevero Paolo

# 2. Usando la lista:
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

# scrivete un for loop che printi una riga come "BoJack Horseman is a horse voiced by Will Arnet." per ogni elemento della lista.

for character in main_characters:
    print(f'{character[0]} is a {character[2]} voiced by {character[1]}')