import numpy as np

class ScrapBooker:
	def crop(self, array, dim, pos = (0, 0)):
		if pos[0] > dim[0] or pos[1] > dim[1]:
			print('error')
		elif dim[0] > len(array) or dim[1] > len(array[0]):
			print('error')
		else:
			return array[pos[0]:dim[0], pos[1]:dim[1]]
		return None
	def thin(self, array, n, axis):
		return np.delete(array, np.s_[::n], axis)
	def juxtapose(self, array, n, axis):
		arr = array
		for i in range(n - 1):
			array = np.concatenate((array, arr), axis)
		return array

	def mosaic(self, array, dim):
		arr = array
		for i in range(dim[1] - 1):
			array = np.concatenate((array, arr), 1)
		arr = array
		for i in range(dim[0] - 1):
			array = np.concatenate((array, arr), 0)
		return array