import numpy as np
from PIL import Image

array=np.zeros([100, 200, 4], dtype=np.uint8)
array[:,:100]=[255, 128, 0, 255] #orage left
array[:,100:]=[0, 0, 255, 255] #blue right

for x in range(200):
    for y in range(100):
        array[y, x, 3]=x

img = Image.fromarray(array)
img.save('testrgba.png')