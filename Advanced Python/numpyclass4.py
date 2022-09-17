import numpy as np
from PIL import Image

img=Image.open('testrgba.png')
array=np.array(img)
print(array.shape)

img = Image.open('testrgb.png')
array=np.array(img)
print(array.shape)

img = Image.open('testgrey.png')
array=np.array(img)
print(array.shape)