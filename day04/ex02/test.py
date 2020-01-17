from ProportionBySport import proportionBySport
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

proportionBySport(data, 2004, 'Tennis', 'F')
#proportionBySport(data, 1996, 'Weightlifting', 'F')
#proportionBySport(data, 1996, 'Weightlifting', 'M')
