from src.DataIngestor import DataIngestor

di = DataIngestor()
m = di.retrieve_single_movie('8012')
print(m)
di.say_hello()
