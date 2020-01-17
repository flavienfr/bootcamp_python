class SpatioTemporalData:
	def __init__(self, df):
		self.df = df

	def when(self, location):
		lst = []
		ndf = self.df
		ndf = ndf[ndf.City == location]
		ndf = ndf.drop_duplicates('Year')
		for index, row in ndf.iterrows():
			lst.append(row['Year'])
		return lst

	def where(self, date):
		ndf = self.df
		ndf = ndf[ndf.Year == date]
		return ndf['City'].iloc[0]