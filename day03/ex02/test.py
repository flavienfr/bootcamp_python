import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ScrapBooker import ScrapBooker

class ImageProcessor:
	def __init__(self):
		pass
	def load(self, path):
		img = mpimg.imread(path)
		print('Loading image of dimensions', len(img[0]), 'x', len(img))
		return np.asarray(img)
	def display(slef, array):
		imgplot = plt.imshow(array)
		plt.show()


imp = ImageProcessor()
arr = imp.load("../ex01/resources/42AI.png")

#ligne colonne
obj = ScrapBooker()

#thin
#array = obj.thin(arr, 2, 1)

#mosaic
#array = obj.mosaic(arr, (5,9))

#juxtapose
#array = obj.juxtapose(arr, 2, 1)

#crop
#array = obj.crop(arr, (100, 100), (50, 50))

imp.display(array)
#print (array)

