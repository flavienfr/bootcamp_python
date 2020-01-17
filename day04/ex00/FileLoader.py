import pandas as pd

class FileLoader:
	def load(self, path):
		data = pd.read_csv(path)
		print('Loading dataset of dimensions', data.shape[0], 'x', data.shape[1])
		return pd.DataFrame(data)

	def display(self, df, n):
		if n > 0:
			print(df[0:n], end = '')
		else:
			print(df[df.shape[0] + n:df.shape[0]], end = '')