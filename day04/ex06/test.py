from FileLoader import FileLoader
from MyPlotLib import MyPlotLib


loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

mpt = MyPlotLib()
features = ['Weight', 'Height']
mpt.histogram(data, ['Weight', 'Height'])
#mpt.density(data, features)