from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

medal = howManyMedalsByCountry(data, 'United States')
print(medal)


medal = howManyMedalsByCountry(data, 'France')
print(medal)