import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class MyPlotLib:
	def histogram(self, data, features):
		for i in range(len(features)):
			data = data.fillna(data.median())
			lst = data[features[i]].values.tolist()
			bins = list(range(int(data[features[i]].min()), int(data[features[i]].max()), 10))
			plt.hist(lst, bins)
			plt.title(features[i])
		plt.tight_layout()
		plt.show()
	
	def density(data, features):
		data = data.fillna(data.median())
		lst = data[features[0]].values.tolist()

		pass

	def pair_plot(data, features):
		pass

	def box_plot(data, features):
		pass