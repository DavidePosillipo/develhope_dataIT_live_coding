s2 = "REDDITO_LAVORO_2023_DIPENDENTE"

for i in s2.split("_"):
    if i.isdigit():
        x = i

print(x)