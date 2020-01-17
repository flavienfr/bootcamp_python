def proportionBySport(df, year, sport, gender):
	df = df[df.Year == year]
	df = df.drop_duplicates('Name', keep='first')#diff between first and last
	total = len(df[df.Sex == gender])
	dfs = df[df.Sex == gender]
	part = len(dfs[dfs.Sport == sport])
	if total == 0:
		print('0')
	else:
		print (part / total)
