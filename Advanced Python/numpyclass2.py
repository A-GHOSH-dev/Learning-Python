import numpy as np
from PIL import Image

array=np.zeros([100, 200, 3], dtype=np.uint8)
array[:,:100]=[255, 128, 0] #orage left
array[:,100:]=[0, 0, 255] #blue right


img = Image.fromarray(array)
img.save('testrgb.png')