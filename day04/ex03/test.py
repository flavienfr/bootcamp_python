from HowManyMedals import howManyMedals
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

dico = howManyMedals(data, 'Usain St. Leo Bolt')
print(dico)
print()
dico = howManyMedals(data, 'Kjetil Andr Aamodt')
print(dico)
