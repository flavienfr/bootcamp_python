from FileLoader import FileLoader

file = FileLoader()

df = file.load('../resources/athlete_events.csv')
print('5 first rows\n')
file.display(df, 5)
print('\n\n5 last rows')
file.display(df, -5)