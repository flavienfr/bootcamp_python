def	youngestFellah(df, year):
	dico = {}
	df = df[df.Year == year]
	dfs = df[df.Sex == 'F']
	dico['Female'] = dfs.Age.min()
	dfs = df[df.Sex == 'M']
	dico['Male'] = dfs.Age.min()
	return dico

