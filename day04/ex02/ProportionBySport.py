def proportionBySport(df, year, sport, gender):
	df = df.drop_duplicates('Name')
	total = len(df[df.Sex == 'F'])
	dfs = df[df.Sex == 'F']
	part = len(df[df.Sport == sport])
	print (part / total)