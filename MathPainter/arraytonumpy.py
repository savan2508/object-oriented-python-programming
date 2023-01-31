import numpy as np
from PIL import Image

data = np.zeros((60, 90, 3), dtype=np.uint8)


# Make it different color
data[0:20] = [255, 103, 31]
data[20:40] = [255, 255, 255]
data[40:60] = [4, 106, 56]

img = Image.fromarray(data, 'RGB')
img.save('indflag_color.png')




