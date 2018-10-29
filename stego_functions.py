import skimage.io as skio
import skimage.color as skc
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import rescale as rescale

def encodeGray(hidden, base, filename):
    # hidden and base are two numpy arrays
    # total number of pixels of hidden must be 1/8 of base
    hpx = hidden.shape[0] * hidden.shape[1]
    bpx = base.shape[0] * base.shape[1]
    base_shape = base.shape
    x = 2
    while(hpx > 1/8 * bpx):
        hidden_new = rescale(hidden, 1/x, anti_aliasing=True, multichannel=False)
        hpx = hidden_new.shape[0] * hidden_new.shape[1]
        x+= 1
    # unravel matrices into arrays
    hidden_new *= 255
    print("hidden shape = ", hidden_new.shape)
    print("hidden length = ", str(hpx))
    hidden = np.reshape(hidden_new, hpx)
    #base = (base*255).astype(int)
    #base = base.astype(int)
    base = np.reshape(base, bpx)
    # iterate through all elements of hidden, keep counter in base, increment for each shift in hidden
    # encode each element in hidden.shape in first 24 lowest bits of base
    hidden_shape = hidden_new.shape
    for i in range(0,2):
        for j in range(0,12):
            element = i * 12 + j
            bit = (np.right_shift(hidden_shape[i], j) & 1)
            #base[element] = np.left_shift(np.right_shift(base[element],1),1) + bit
            base[element] = ((base[element] // 2) * 2) +  bit
    # encode remaining bits in
    count = 24
    for x in range(0, len(hidden)):
        for j in range(0,8):
            bit = (int(hidden[x]) >> j) & 1
            #base[count] = np.left_shift(np.right_shift(base[count],1),1) + bit
            base[count] = ((base[count] // 2) * 2) + bit
            count += 1
    base = np.reshape(base, base_shape)
    skio.imsave(filename, base)

def decodeGray(base, filename):
    # base is a 2D numpy array
    # first 2 12 byte intervals refer to shape of the hidden image
    bpx = base.shape[0] * base.shape[1]
    base = np.reshape(base, bpx)
    shape = [0, 0]
    for i in range(0,2):
        for j in range(0,12):
            bit = base[i * 12 + j] & 1
            shape[i] = shape[i] | ((2**j)* bit)
    print("shape = ", shape)
    length = shape[0] * shape[1]
    hidden = np.zeros(length, dtype="int8")
    # decode next length*8 bytes
    count = 0
    for x in range(24, length * 8):
            bit = base[x] & 1
            location = (x-24)//8
            hidden[location] = hidden[location] | ((2**count)*bit)
            count = (count + 1) % 8
    hidden_new = np.reshape(hidden, (shape[0], shape[1]))
    skio.imsave(filename, hidden_new)
