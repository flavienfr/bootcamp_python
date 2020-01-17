
class AdvancedFilter:
	def mean_blur(self, arr):
		s_arr = arr
		pat = nb.array()
		arr[0:3, 0:3].sum() / 9
		for i in range(3):
			pat += s_arr[0][i]
		for i in range(3):
			pat += s_arr[i][0]
		pat /= 6
		arr[0][0] = pat
