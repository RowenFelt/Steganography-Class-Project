import skimage.io as skio
import skimage.color as skc
import skimage.morphology as skm
from skimage import feature
import matplotlib.pyplot as plt
import skimage.measure as skms
import numpy as np
from scipy.ndimage.filters import convolve
from stego_functions import saveDecodedGray
import glob
import os



def nat_img_dect1(img, debug=False):
    """detects whether an image is just random noise or a natural image using region analysis"""
    natural = False

    lbl = skm.label(img)

    areaMax = max([p.area for p in skms.regionprops(lbl)])

    if debug:
        clean = skm.remove_small_objects(lbl, min_size=areaMax)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
        ax1.imshow(img, cmap='gray')
        ax1.set_title('Original')
        ax2.imshow(skc.label2rgb(clean))
        ax2.set_title('Blob coloring')
        plt.show()

    print(areaMax)

    if areaMax > 100:
        natural = True

    return natural


def nat_img_dect2(img, debug=False):
    """detects whether an image is just random noise or a natural image using convolution
    edge detection"""
    natural = False
    kernel = np.asarray([[0,1,0],
                    [1,-4,1],
                    [0,1,0]], dtype='float')

    img_norm = (img - img.min()) / (img.max() - img.min())

    edges = convolve(img_norm, kernel)
    edges2 = convolve(edges, kernel)

    if debug:
        fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(16,16))
        ax1.imshow(img, cmap='gray')
        ax2.imshow(edges2, cmap='gray')
        plt.show()


        print(edges.max() - edges.min())

    range = edges.max() - edges.min()


    if range < 5:
        natural = True

    return natural


def nat_img_dect3(img, debug=False):
    """detects whether an image is just random noise or a natural image using Canny
    edge detection"""
    natural = False

    #sigma = 3, takes away lot of the edges, and leaves noisy images black
    edges = feature.canny(img, 5)


    if debug:
        print(sum(edges.flat))
        fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(16,16))
        ax1.imshow(img, cmap='gray')
        ax2.imshow(edges, cmap='gray')
        plt.show()
        print(sum(edges.flat))

    if sum(edges.flat) > 100:
        natural = True

    return natural

def nat_img_dect4(img, debug=False):
    """detects whether an image is just random noise or a natural image using convolution
    edge detection, then connected components analysis"""
    natural = False
    kernel = np.asarray([[0,1,0],
                    [1,-4,1],
                    [0,1,0]], dtype='float')

    img_norm = (img - img.min()) / (img.max() - img.min())

    edges = convolve(img_norm, kernel)

    lbl = skm.label(edges)

    areaMax = max([p.area for p in skms.regionprops(lbl)])

    if debug:
        clean = skm.remove_small_objects(lbl, min_size=areaMax)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
        ax1.imshow(img, cmap='gray')
        ax1.set_title('Original')
        ax2.imshow(skc.label2rgb(lbl))
        ax2.set_title('Blob coloring')
        plt.show()

        print(areaMax)

    if areaMax <= 5:
        natural = True

    return natural

def test_encoders():
    """This function runs all the natural image detectors on a set of images"""
    # file = open('stego_encoders/results_natural_image_detector_decoded.txt', 'w')
    # file.write('image\tr1\tr2\tr3\tr4\n')

    file = open('stego_encoders/conv_mean_test.txt', 'w')
    file.write('image\tr1\n')
    images = glob.glob("stego_encoders/decoded_imgs/*.*")
    images2 = glob.glob("stego_encoders/testing_images/*.*")

    for image in images2:
        img = skio.imread(image)
        try:
            r2 = nat_img_dect2(img)
        except Exception as e:
            r2 = "fail"
        line = '\t'.join([str(image), str(r2)] )
        print(line)
        file.write(line + '\n')

    for image in images:
        img = skio.imread(image)
        try:
            r2 = nat_img_dect2(img)
        except Exception as e:
            r2 = "fail"
        line = '\t'.join([str(image), str(r2)] )
        print(line)
        file.write(line + '\n')

    # for image in images:
    #     img = skio.imread(image)
    #     try:
    #         r1 = nat_img_dect1(img)
    #     except Exception as e:
    #         r1 = "fail"
    #     try:
    #         r2 = nat_img_dect2(img)
    #     except Exception as e:
    #         r2 = "fail"
    #     try:
    #         r3 = nat_img_dect3(img)
    #     except Exception as e:
    #         r3 = "fail"
    #     try:
    #         r4 = nat_img_dect4(img)
    #     except Exception as e:
    #         r4 = "fail"
    #
    #     line = '\t'.join([str(image), str(r1), str(r2), str(r3), str(r4)] )
    #     print(line)
    #     file.write(line + '\n')

def make_test_images():
    images = glob.glob("stego_encoders/testing_images/*.*")
    i = 0

    for image in images:
        img = skio.imread(image)
        img_g = skc.rgb2gray(img)
        img_g *= 255
        img2 = img_g.astype(np.uint8)
        print(img_g.shape)
        filename = "stego_encoders/decoded_imgs/decoded_" + str(i)
        i+=1
        try:
            decoded = saveDecodedGray(img2, filename)
        except Exception as e:
            pass




def main():
    """using main to run my testing"""

    # mandrill = skio.imread('mandrill.png')
    #
    # noise = skio.imread('noise.png')
    #
    # cameraman = skio.imread('cameraman.png')
    #
    # planks = skio.imread('Planks.tif')
    #
    # newhouse = skio.imread('newhouse.png')

    #bed = skio.imread('Hidden_image.png')

    #decoded = decodeGray(mandrill)
    # img = skio.imread('lamp.JPG')
    #img_g = skc.rgb2gray(img) * 255
    #
    # img2 = img_g.astype(np.uint8)
    # decoded = saveDecodedGray(img2, "decoded_2")
    #decoded = skio.imread('decoded_1.png')

    #decode images that are 4000,5000 pixels

    # plt.figure(figsize=(10,10))
    # plt.imshow(decoded, cmap='gray')

    #img = skc.rgb2gray(decoded)

    #print(nat_img_dect2(mandrill, True))

    test_encoders()
    #make_test_images()




main()
