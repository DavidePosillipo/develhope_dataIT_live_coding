s2 = "REDDITO_LAVORO_2023_DIPENDENTE"
split = s2.split("_")
i = 0
for i in range(0,len(split)):
    if split[i].isdigit():
        print(split[i])
    else: 
        i += 1
