from retrieve_cast import retrieve_cast
from imdb import Cinemagoer

ia = Cinemagoer()

movies_id = ['8012', '12929', '6768', '25214882', '0499549']

'''
# Codice di esempio di utilizzo della funzione retrieve_cast
movies_cast = {}

for movie_id in movies_id:
	print(movie_id)
	movies_cast[movie_id] = retrieve_cast(movie_id, ia)

print(movies_cast)
'''


'''
# Utilizzando la funzione già pronta retrieve_cast, creare una funzione che:
1. per ogni film della lista movies_id, fornisca il numero totale di attori
2. aggiungere un parametro che permetta di scegliere dalla lista un film specifico usando il suo id. La funzione restituisce il numero totale di attori solo per il film scelto
	- se il film scelto non è presente nella lista, la funzione restituisce un messaggio e si interrompe
3. aggiungere un parametro booleano per restituire un dizionario con i soli nomi degli attori in uppercase
4.[BONUS] aggiungere un parametro numerico per restituire solo i film usciti dopo l'anno indicato dal parametro
'''

# INSERISCI QUI SOTTO LA TUA SOLUZIONE

