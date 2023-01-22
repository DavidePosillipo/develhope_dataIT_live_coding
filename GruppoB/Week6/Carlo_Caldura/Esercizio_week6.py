##TODO Trovare l'anno all'interno della stringa s2 in modo indipendente dalla posizione dell'anno all'interno della stringa

s2 = "REDDITO_LAVORO_2021_DIPENDENTE"
print(s2.join([anno for anno in s2.split("_") if anno.isdigit()]))
