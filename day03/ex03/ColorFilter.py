import numpy as np

class ColorFilter:
	def invert(self, array):
		if len(array[0][0]) == 4:
			return [1, 1, 1, 2] - array # work only witch [r,g,b,1]
		else:
			return [1, 1, 1] - array
	def to_blue(self, array):
		if len(array[0][0]) == 4:
			return array * [0, 0, 1, 1]
		else:
			return array * [0, 0, 1]
	def to_green(self, array):
		if len(array[0][0]) == 4:
			return array * [0, 1, 0, 1]
		else:
			return array * [0, 1, 0]
	def to_red(self, array):
		if len(array[0][0]) == 4:
			return array * [1, 0, 0, 1]
		else:
			return array * [1, 0, 0]
	def celluloid(self, array):
		return None