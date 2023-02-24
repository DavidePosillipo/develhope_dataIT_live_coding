def retrieve_cast(movie_id, cinemagoer_instance):
	'''
	Function that retrieves cast information for the movie with movie_id. 
	It retrieves for each actor the name of her/his character, if available. 
	If not available, it returns a string "N.A." (not available).
	If more roles are available for the same actor, it retrieves the first one 
	showed by the API. 

	Args:
		movie_id: string with the IMDB id of the movie
		cinemagoer_instance: instance of the Cinemagoer class

	Returns:
		A dict mapping names of the actors with the names of their characters.
	'''

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
