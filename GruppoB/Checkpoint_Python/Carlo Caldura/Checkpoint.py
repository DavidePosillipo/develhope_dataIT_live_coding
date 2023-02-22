from retrieve_cast import retrieve_cast
from imdb import Cinemagoer

ia = Cinemagoer()

movies_id = ['8012', '12929', '6768', '25214882', '0499549']


# Codice di esempio di utilizzo della funzione retrieve_cast
movies_cast = {}
new_dict = {}
for movie_id in movies_id:
    #print(movie_id)
    movies_cast[movie_id] = retrieve_cast_davide(movie_id, ia)
#print(movie_cast)
#print(new_dict)
movies_cast
        

input1 = input(f'Given these movie ids {movies_id} select the one you want to retrive: ')
input2 = input(f'Would you like to retrive the {input1} cast in upper case? \nType in y or n:\n')
year = (input(f'Type the year you would like the movie to be released after: \n'))


def new_function(input, year, input2):

    if year:

        movies_id_year = [movie for movie in movies_id if ia.get_movie(movie).get('year') >= int(year)]


        if len(movies_id_year) > 1:     
            print(f'The movies released after year {year} are {movies_id_year}')
            
        else :
            print(f'The only movie released after year {year} is {movies_id_year}')

    
    while movie_id in movies_id:
        

        if input in movies_id:
            print(f'The number of actors cast in the movie with movie id {input} is {len(movies_cast[input])}.')

            
            if input2 == 'y':
              
                new_dict = {k.upper() : v for k, v in (movies_cast[input]).items()}
                print(f'Dictionary with actors in upper case: {new_dict}')
                
            else :
              
                print(f'Dictionary with actors not in upper case: {movies_cast[input]}')

        else:
            print('Sorry, Id was not found')

        break

new_function(input1, year, input2)
