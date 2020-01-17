from YoungestFellah import youngestFellah
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(youngestFellah(data, 1992))