import numpy as np

class NumPyCreator:
	def from_list(self, lst):
		return np.asarray(lst)
	def from_tuple(self, tpl):
		return np.asarray(tpl)
	def from_iterable(self, itr):
		return np.asarray(itr)
	def from_shape(self, shape, value = 0):
		return np.full(shape, value)
	def random(self, shape):
		return np.random.rand(*shape)
	def identity(self, n):
		return np.identity(n)

npc = NumPyCreator()
res = npc.from_list([[1,2,3],[6,3,4]])
print(res)

res = npc.from_tuple(("a", "b", "c"))
print(res)

res = npc.from_iterable(range(5))
print(res)

shape = (3,5)
res = npc.from_shape(shape)
print(res)

res = npc.random(shape)
print(res)

res = npc.identity(4)
print(res)