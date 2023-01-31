import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        #     Create a numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        #         Convert the array to canvas using PIL Image
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
