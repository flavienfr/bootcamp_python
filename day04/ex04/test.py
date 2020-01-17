from SpatioTemporalData import SpatioTemporalData
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

std = SpatioTemporalData(data)
print(std.when('Paris'))
print(std.when('Athina'))

print(std.where(1900))
print(std.where(2016))
print(std.where(1896))