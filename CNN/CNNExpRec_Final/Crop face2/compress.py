import numpy as np
import os
from skimage import io,data,color
from scipy.misc import imresize
import matplotlib.image
text = open('bbox.txt')
for line in text.readlines():
    content = line.split()
    Path = content[0]
    tmp = Path
    Path = 'gray image/' + Path[6] + '/' + Path[8:]
    Path2 = 'gray image small/' + tmp[6] + '/' + tmp[8:]
    image = matplotlib.image.imread(Path)
    image = imresize(image, (48,48))  # compress to 48*48 pixel
    io.imsave(Path2,image)
