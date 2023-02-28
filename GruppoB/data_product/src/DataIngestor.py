from imdb import Cinemagoer

class DataIngestor:

    def __init__(self):
        self.cinemagoer_istance = Cinemagoer()
        print(self.cinemagoer_istance)

    def retrieve_single_movie(self, id):
        movie = self.cinemagoer_istance.get_movie(id)
        return movie

    def say_hello(self):
        print("hello world")
