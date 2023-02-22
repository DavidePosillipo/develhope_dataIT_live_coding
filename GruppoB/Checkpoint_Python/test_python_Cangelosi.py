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
#INSERISCI QUI SOTTO LA TUA SOLUZIONE
#esercizio2
def actor_movie(movies_id, id_film = None, upper = False):

	dict_cast = {}
	
	#esercizio1, creo la funzione che restituisce un dizionario con i film della lista e la relativa numerosita' del cast
	def len_movies():
		for film in movies_id:
			len_cast = len(retrieve_cast(film,ia))
			dict_cast[ia.get_movie(film)['title']] = len_cast
		return "Ecco la numerosita' del cast dei seguenti film", dict_cast
	
	#esercizio 3,creo la funzione che restituisce in upper i nomi degli attori.
	def upper_retrieve_cast():
		if upper == True:
			dict_upper = { k.upper():v for (k,v) in zip(retrieve_cast(id_film,ia).keys(), retrieve_cast(id_film,ia).values())} 
			return dict_upper						
	
	"""esercizio 2, creo la funzione aggiunge il parametro per far selezionare il film di cui 
	restituisce la lunghezza del cast e richiamo la funzione upper retrieve cast al suo interno"""
	
	def selected_film():
		if id_film in movies_id:
			len_cast = len(retrieve_cast(id_film,ia))
			return f"il cast del film {ia.get_movie(id_film)} e' di {len_cast} attori", upper_retrieve_cast()

		else:
			print("errore")

	return len_movies(),selected_film()
	
		


print(actor_movie(movies_id,'8012',True))


