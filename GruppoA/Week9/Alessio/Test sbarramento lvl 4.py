def retrieve_cast(movie_id, cinemagoer_instance):
    movie = cinemagoer_instance.get_movie(movie_id)
    movie_cast = {}

    if 'cast' in movie.keys(): # some movies have no cast info
        for actor in movie['cast']:
            try:
                first_role = actor.currentRole[0] if isinstance(actor.currentRole, list) else actor.currentRole
                movie_cast[actor['name']] = first_role.data['name']
            except KeyError:
                movie_cast[actor['name']] = "N.A."

    return movie_cast

from imdb import Cinemagoer

ia = Cinemagoer()

movies_id = ['8012', '12929', '6768', '25214882', '0499549']

# Utilizzando la funzione già pronta retrieve_cast, creare una funzione che:
#1. per ogni film della lista movies_id, fornisca il numero totale di attori
#2. aggiungere un parametro che permetta di scegliere dalla lista un film specifico usando il suo id. 
#   La funzione restituisce il numero totale di attori solo per il film scelto
#   se il film scelto non è presente nella lista, la funzione restituisce un messaggio e si interrompe
#3. aggiungere un parametro booleano per restituire un dizionario con i soli nomi degli attori in uppercase
#4.[BONUS] aggiungere un parametro numerico per restituire solo i film usciti dopo l'anno indicato dal parametro

def f1(movielist):
    diz = {}
    for i in movielist:
        movie_cast = retrieve_cast(i,ia)
        diz[i] = len(movie_cast)
    return diz

def f2(movielist, my_movie_id=None):
    if my_movie_id is None:
        diz = {}
        for i in movielist:
            movie_cast = retrieve_cast(i,ia)
            diz[i] = len(movie_cast)
        return diz
    elif my_movie_id not in movielist:
        return('F2 Error: movie not in list')        
    elif my_movie_id in movielist:
        diz = {}               
        movie_cast = retrieve_cast(my_movie_id,ia)
        diz[my_movie_id] = len(movie_cast)
        return diz


def f3(movielist, my_movie_id=None, names=False):
    if names:
        if my_movie_id not in movielist:
            return('F3 Error: 1 argument missing "my_movie_id"')
        else:
            actorsupper = {}
            movie_cast = retrieve_cast(my_movie_id,ia)
            for i in movie_cast:
                actorsupper.update({i.upper():'is our guy'})
            return actorsupper           
    else:
        return f2(movielist,my_movie_id)


def f4(movielist, my_movie_id=None, names=False, date=None):
    if date:
        movie_year = {}
        new_movie_list = []
        for i in movielist:
            if ia.get_movie(i)['year'] >= date:
                movie_year.update({i:ia.get_movie(i)['year']})
                new_movie_list.append(i)
        # print (new_movie_list)
        # print (movie_year) # code working so far        
        return f3(new_movie_list,my_movie_id, names)
    else:
        return f3(movielist, my_movie_id, names)

print(f4(movies_id, None, False, 2000))