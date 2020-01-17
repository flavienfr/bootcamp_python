def howManyMedals(df, name):
	dico = {}
	df = df[df.Name == name]
	for index, row in df.iterrows():
		if not row['Year'] in dico:
			med = {'G': 0, 'S': 0, 'B': 0}
		if row['Medal'] == 'Gold':
			med['G'] += 1
		elif row['Medal'] == 'Silver':
			med['S'] += 1
		elif row['Medal'] == 'Bronze':
			med['B'] += 1
		dico[row['Year']] = med
	return dico
