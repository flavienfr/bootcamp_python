def	youngestFellah(df, year):
	dico = {}
	dfs = df[df.Sex == 'F']
	dico['Female'] = dfs.Age.min()
	dfs = df[df.Sex == 'M']
	dico['Male'] = dfs.Age.min()
	return dico

