#creare un dizionario che ha come chiave il nome 
# dell'attore e come contenuto il ruolo

import imdb
ia = imdb.Cinemagoer()
#movie = ia.search_movie('')

def cast():
    dictcast={}
    film = input('inserire il film:')
    movie = ia.search_movie(film)
    #print(movie)

    for elemento in movie:
        print (elemento)
        scelta=input('Premi ok se hai trovato il film che desideravi, altrimenti passa avanti con un tasto qualsiasi e premi invio:')
        if scelta == 'ok':
            movie = elemento
            break  

    #filmcode=input('inserire il codice esatto del film:')
    
    moviecode= ia.get_movie(movie.movieID)
    
    #print(type(moviecode['cast']))
    
    for i in range(len(moviecode['cast'])):
        actorcode=moviecode['cast'][i]
        actor=actorcode['name']
        dictcast[actor]=actorcode.currentRole.data['name']
        #x=x+1
    return print(dictcast)        


cast()
