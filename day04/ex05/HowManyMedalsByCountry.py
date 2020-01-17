def howManyMedalsByCountry(df, country):
	dico = {}
	df = df[df.Team == country]
	df = df.sort_values(by=['Year'])
	#df = df.drop_duplicates('Event', keep='first')
	#How to sort duplicates in each Year separatly
	for index, row in df.iterrows():
		if not row['Year'] in dico:
			dico[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
		if row['Medal'] == 'Gold':
			dico[row['Year']]['G'] += 1
		elif row['Medal'] == 'Silver':
			dico[row['Year']]['S'] += 1
		elif row['Medal'] == 'Bronze':
			dico[row['Year']]['B'] += 1
	return dico
