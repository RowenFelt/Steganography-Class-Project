import skimage.io as skio
import skimage.color as skc
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import rescale as rescale

def encodeGray(hidden, base):
    # hidden and base are two numpy arrays
    # Check the datatypes
    print("hidden.dtype",hidden.dtype)
    if((hidden.dtype != "float64") or (base.dtype != "float64")):
        raise TypeError('Both matrices must be type float64')
    # total number of pixels of hidden must be 1/8 of base
    base = (base*255).astype(int)
    hpx = hidden.shape[0] * hidden.shape[1]
    bpx = base.shape[0] * base.shape[1]
    base_shape = base.shape
    x = 1
    while(hpx > 1/8 * bpx):
        hpx = hidden.shape[0]/x * hidden.shape[1]/x
        x+= 1
    hidden_new = rescale(hidden, 1/(x-1), anti_aliasing=True, multichannel=False)
    hpx = hidden_new.shape[0] * hidden_new.shape[1]
    # unravel matrices into arrays
    print("hidden shape = ", hidden_new.shape)
    print("hidden length = ", str(hpx))
    hidden_new *= 255
    hidden = np.reshape(hidden_new, hpx)
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
    return base

def decodeGray(base):
    # base is a 2D numpy array
    if(base.dtype != "uint8"):
        raise TypeError('Base must be a numpy matrix of type uint8')
    # first 2 12 byte intervals refer to shape of the hidden image
    bpx = base.shape[0] * base.shape[1]
    base = np.reshape(base, bpx)
    print("base after reshape = ",base)
    shape = [0, 0]
    for i in range(0,2):
        for j in range(0,12):
            bit = base[i * 12 + j] & 1
            shape[i] = shape[i] | ((2**j)* bit)
    print("shape = ", shape)
    length = shape[0] * shape[1]
    #check length against actual size of base image
    if(length > (bpx - 24)):
        print("Theoretical hidden image is too large to be encoded in base image")
        return False
    hidden = np.zeros(length, dtype="uint8")
    # decode next length*8 bytes
    count = 0
    base = base & 1 #converts to least significant bits only
    for x in range(24, length * 8):
        location = (x-24)//8
        hidden[location] = hidden[location] | ((2**count)*base[x])
        count = (count + 1) % 8
    hidden_new = np.reshape(hidden, (shape[0], shape[1]))
    print("hidden_new", hidden_new)
    return hidden_new

def saveEncodedGray(base, hidden, filename):
    encoded = encodeGray(base, hidden)
    if(type(encoded) is not np.ndarray):
        return False
    savename = filename + ".png"
    skio.imsave(savename, encoded)

def saveDecodedGray(base, filename):
    decoded = decodeGray(base)
    if(type(decoded) is not np.ndarray):
        return False
    savename = filename + ".png"
    skio.imsave(savename, decoded)

def encodeColor(hidden, base):
    # base and hidden must both be color images with values between 0-255
    if(base.dtype != "uint8" or hidden.dtype != "uint8"):
        raise TypeError('Base and Image must both be int arrays')
    base = base.astype("float64")
    hidden = hidden.astype("float64")
    base = base/255
    hidden = hidden/255
    colors = ["red", "green", "blue"]
    basefields = {}
    hiddenfields = {}
    for color in range(0,len(colors)):
        basefields[colors[color]] = base[:,:,color]
        hiddenfields[colors[color]] = hidden[:,:,color]
    for color in colors:
        basefields[color + "encoded"]= encodeGray(hiddenfields[color], basefields[color])
        if(type(basefields[color + "encoded"]) is not np.ndarray):
            return False
    return np.dstack((basefields["redencoded"],basefields["greenencoded"],basefields["blueencoded"]))

def decodeColor(base):
    # base must both be color images with values between 0-255
    if(base.dtype != "uint8"):
        raise TypeError('Base must both be int arrays')
    base = base.astype("float64")
    base = base/255
    hidden = hidden/255
    colors = ["red", "green", "blue"]
    basefields = {}
    hiddenfields = {}
    for color in range(0,len(colors)):
        basefields[colors[color]] = base[:,:,color]
        hiddenfields[colors[color]] = hidden[:,:,color]
    for color in colors:
        basefields[color + "encoded"]= encodeGray(hiddenfields[color], basefields[color])
        if(type(basefields[color + "encoded"]) is not np.ndarray):
            return False
    return np.dstack((basefields["redencoded"],basefields["greenencoded"],basefields["blueencoded"]))


def saveEncodedColor(base, hidden, filename):
    encoded = encodeColor(hidden, base)
    if(type(encoded) is not np.ndarray):
        return False
    savename = filename + ".png"
    skio.imsave(savename, encoded)

def saveDecodedColor(base, filename):
    decoded = decodeColor(base)
    if(type(decoded) is not np.ndarray):
        return False
    savename = filename + ".png"
    skio.imsave(savename, decoded)

