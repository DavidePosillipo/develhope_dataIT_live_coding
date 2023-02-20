'''
# Utilizzando la funzione già pronta retrieve_cast, creare una funzione che:
1. per ogni film della lista movies_id, fornisca il numero totale di attori
2. aggiungere un parametro che permetta di scegliere dalla lista un film specifico usando il suo id. La funzione restituisce il numero totale di attori solo per il film scelto
	- se il film scelto non è presente nella lista, la funzione restituisce un messaggio e si interrompe
3. aggiungere un parametro booleano per restituire un dizionario con i soli nomi degli attori in uppercase
4.[BONUS] aggiungere un parametro numerico per restituire solo i film usciti dopo l'anno indicato dal parametro
'''
def retrieve_cast(movie_id, cinemagoer_instance):                                                                   #Function that retrieves cast information for the movie with movie_id.
	movie = cinemagoer_instance.get_movie(movie_id)                                                                 #It retrieves for each actor the name of her/his character, if available.
	movie_cast = {}                                                                                                 #If not available, it returns a string "N.A." (not available).                                                                                                  
                                                                                                                    #If more roles are available for the same actor, it retrieves the first one
	if 'cast' in movie.keys(): # some movies have no cast info                                                      #showed by the API.
		for actor in movie['cast']:                                                                                 #Args:
			try:                                                                                                    #	movie_id: string with the IMDB id of the movie
				first_role = actor.currentRole[0] if isinstance(actor.currentRole, list) else actor.currentRole     #	cinemagoer_instance: instance of the Cinemagoer class
				movie_cast[actor['name']] = first_role.data['name']                                                 #Returns:
			except KeyError:                                                                                        #	A dict mapping names of the actors with the names of their characters.
				movie_cast[actor['name']] = "N.A."

	return movie_cast

	
from imdb import Cinemagoer
                                                                                                                    #Codice di esempio di utilizzo della funzione retrieve_cast
ia = Cinemagoer()                                                                                                   # movies_cast = {}
movies_id = ['8012', '12929', '6768', '25214882', '0499549']                                                        # for movie_id in movies_id:
                                                                                                                    #     print(movie_id)
#MY SOLUTION                                                                                                        #     movies_cast[movie_id] = retrieve_cast(movie_id, ia)
def num_actors(movies, id = None, max_year = None, upper_names = False):
    dct = {}

    for movie in movies:
        cast_movie = retrieve_cast(movie, ia)
        dct_cast = {}
        if id:
            if id in movies:
                id_cast = retrieve_cast(id, ia)
                if upper_names:
                    for key, value in id_cast.items():
                        dct_cast[key.upper()] = value
                    dct.update({f"{id} - " + str(ia.get_movie(id)): (len(dct_cast), dct_cast)})  
                else:
                    for key, value in id_cast.items():
                        dct.update({f"{id} - " + str(ia.get_movie(id)): (len(id_cast), id_cast)})
                return (dct if ia.get_movie(id)["year"] >= max_year else f"The movie with ID {id} was realeased before the year {max_year}") if max_year else dct
            else: 
                return "ID not in movie list"
        elif max_year:
            if upper_names:
                if ia.get_movie(movie)["year"] >= max_year:
                    for key, value in cast_movie.items():
                        dct_cast[key.upper()] = value
                    dct[f"{movie} - " + str(ia.get_movie(movie)) + " - " + str(ia.get_movie(movie)["year"])] = (len(dct_cast), dct_cast)
            elif ia.get_movie(movie)["year"] >= max_year:
                dct.update({f"{movie} - " + str(ia.get_movie(movie)) + " - " + str(ia.get_movie(movie)["year"]) : (len(cast_movie), cast_movie)})
            else:
               f"All movies in the list were released before {max_year}"
        else: 
            if upper_names:
                for key, value in cast_movie.items():
                    dct_cast.update({key.upper(): value})
                dct.update({f"{movie} - " + str(ia.get_movie(movie)): (len(dct_cast), dct_cast)})
            else:
                for key, value in cast_movie.items():
                    dct_cast.update({key.upper(): value})
                dct.update({f"{movie} - " + str(ia.get_movie(movie)): (len(cast_movie), dct_cast)})
        
    return f"All movies in the list were released before {max_year} " if max_year and upper_names and dct == {} else dct

print(num_actors(movies_id, None, 2000))



    
""" ls = {}
    dct = {}
    
    if only_names:
        for movie in movies:
            cast = retrieve_cast(movie, ia)
            for key, value in cast.items():
                dct[key.upper()] = value
        return dct
    elif id in movies:
        cast = retrieve_cast(id, ia)
        dct[id] = len(cast)
        return dct
    elif id == None:
        if max_year:
            for movie in movies:
                year = ia.get_movie(movie)["year"]
                if year >= max_year:
                    cast = retrieve_cast(movie, ia)
                    dct[movie] = len(cast.keys())
        else:
            for movie in movies:
                cast = retrieve_cast(movie, ia)
                dct[movie] = len(cast.keys())
        return dct
    else: 
        return "ID not present"
        
print(num_actors(movies_id, None, 2000, True))"""


#exe1 w/ list
"""def num_actors(movies):   
    ls = {}
    for movie in movies:
        cast = retrieve_cast(movie, ia)
        ls[movie] = len(cast.keys())
    return ls

print(num_actors(movies_id))"""

#exe2 with dictionary instead of list
'''def num_actors(movies, id = None):   
    ls = {}
    if id in movies:
        cast = retrieve_cast(id, ia)
        return len(cast)
    elif id == None:
        for movie in movies:
            cast = retrieve_cast(movie, ia)
            ls[movie] = len(cast.keys())
        return ls
    else: 
        return "ID not present"
        
print(num_actors(movies_id))'''





#???????
"""if max_year:
        for movie in movies:
            title = ia.get_movie(movie)
            title_year = title["year"]
            if title['year'] >= max_year:
                cast = retrieve_cast(movie, ia)
                ls.clear()
                ls[f"{title}(id={movie}) - {title_year}"] = cast
                dct.update(ls)
        return dct if len(dct) > 0 else f"no movie in the movies list was produced in {max_year} or after"
        """

 