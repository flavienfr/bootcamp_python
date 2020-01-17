def proportionBySport(df, year, sport, gender):
	df = df.drop_duplicates('Name')
	df = df[df.Year == year]
	total = len(df[df.Sex == gender])
	dfs = df[df.Sex == gender]
	part = len(dfs[dfs.Sport == sport])
	if total == 0:
		print('0')
	else:
		print (part / total)
