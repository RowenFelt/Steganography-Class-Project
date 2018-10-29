import skimage.io as skio
import skimage.color as skc
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import rescale as rescale

bed = skio.imread('bed.jpg')
bedg = skc.rgb2gray(bed)

house = skio.imread('house.JPG')
houseg = skc.rgb2gray(house)

encodeGray(bedg, houseg, 'newhouse.png')
new_house = skio.imread('newhouse.png')

decodeGray(new_house, "Hidden_image.png")


