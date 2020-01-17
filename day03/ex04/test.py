from AdvancedFilter import AdvancedFilter
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("resources/42AI.png")

obj = AdvancedFilter()
obj.mean_blur(arr)

#imp.display(arr)
