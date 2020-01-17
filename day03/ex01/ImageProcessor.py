import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

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
arr = imp.load("resources/small_img_1.png")
print(arr)
imp.display(arr)