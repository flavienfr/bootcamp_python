from ProportionBySport import proportionBySport
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

proportionBySport(data, 2004, 'Tennis', 'F')