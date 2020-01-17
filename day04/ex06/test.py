from FileLoader import FileLoader
from MyPlotLib import MyPlotLib


loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

mpt = MyPlotLib()
mpt.histogram(data, ['Weight', 'Height'])