class Vector:
	def __init__(self, init):
		if type(init) is list:
			#potection anti str
			self.values = init;
			self.size = len(init)
		elif type(init) is int:
			self.values = list(range(init))
			self.size = init
		elif type(init) is tuple:
			if len(init) == 2:
				self.values = list(range(init[0], init[1]))
				self.size = len(init)
			else:
				print('bad range')
		self.values = [float(i) for i in self.values]

	def __add__(self, nb):
		if type(nb) is Vector:
			if self.size == nb.size:
				for i in range(self.size):
					self.values[i] += nb.values[i]
			else:
				print('Vectors are not equals size')
				return
		else:
			for i in range(self.size):
				self.values[i] += nb
		return self.values
	def __radd__(self, nb):
		if type(nb) is Vector:
			if self.size == nb.size:
				for i in range(self.size):
					self.values[i] += nb.values[i]
			else:
				print('Vectors are not equals size')
				return
		else:
			for i in range(self.size):
				self.values[i] += nb
		return self.values

	def __sub__(self, nb):
		if type(nb) is Vector:
			if self.size == nb.size:
				for i in range(self.size):
					self.values[i] -= nb.values[i]
			else:
				print('Vectors are not equals size')
				return
		else:
			for i in range(self.size):
				self.values[i] -= nb
		return self.values
	def __rsub__(self, nb):
		if type(nb) is Vector:
			if self.size == nb.size:
				for i in range(self.size):
					self.values[i] -= nb.values[i]
			else:
				print('Vectors are not equals size')
				return
		else:
			for i in range(self.size):
				self.values[i] -= nb
		return self.values

	def __truediv__(self, nb):
		if type(nb) is Vector:
			print("only scalars.")
			return
		else:
			for i in range(self.size):
				if nb == 0:
					print("Can't substract by 0")
					return	
				self.values[i] /= nb				
			return self.values
	def __rtruediv__(self, nb):
		if type(nb) is Vector:
			print("only scalars.")
			return
		else:
			for i in range(self.size):
				if nb == 0:
					print("Can't substract by 0")
					return	
				self.values[i] /= nb				
			return self.values

	def __mul__(self, nb):
		if type(nb) is Vector:
			if self.size == nb.size:
				tmp = 0
				for i in range(self.size):
					tmp += self.values[i] * nb.values[i]
				self.values = tmp
			else:
				print('Vectors are not equals size')
				return
		else:
			for i in range(self.size):
				self.values[i] *= nb
		return self.values
	def __rmul__(self, nb):
		if type(nb) is Vector:
			if self.size == nb.size:
				tmp = 0
				for i in range(self.size):
					tmp += self.values[i] * nb.values[i]
				self.values = tmp
			else:
				print('Vectors are not equals size')
				return
		else:
			for i in range(self.size):
				self.values[i] *= nb
		return self.values
	
	def __str__(self):
		return "values: {}\size: {}".format(self.values, self.size)
