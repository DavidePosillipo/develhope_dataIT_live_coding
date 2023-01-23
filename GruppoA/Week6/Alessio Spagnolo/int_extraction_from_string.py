s6 = "REDDITO_DIPENDENTE_DELL_ANNO_2021"

# Metodo 1

s6split = s6.split('_')
anno = [int(x) for x in s6split if x.isdigit()]
print (f'L\'anno in questione è {anno}')

# Metodo 2

for i in s6split:
    if i.isdigit():
        print(f"L'anno di riferimento è {i}")