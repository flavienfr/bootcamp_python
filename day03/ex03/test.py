from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("resources/42AI.png")

cf = ColorFilter()

#arr = cf.invert(arr)
arr = cf.to_green(arr)
#arr = cf.to_red(arr)
#arr = cf.to_blue(arr)
#arr = cf.to_celluloid(arr)
#arr = cf.to_grayscale(arr, 'm')
#arr = cf.to_grayscale(arr, 'weigthed')

imp.display(arr)
