#importing needed libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import cv2

#loading the dataset
data = np.load("https://zenodo.org/record/6496656/files/chestmnist.npz")

#creating a dictionary of the image with each set in a key:value pair
data = dict(data)

#choosing the image we analyze
image = data["train_images"][100]


#converting a 1-channel image (1 value per pixel) to 3-channel one to analyze and apply filters
#https://stackoverflow.com/questions/14786179/how-to-convert-a-1-channel-image-into-a-3-channel-with-opencv2
img = cv2.merge((image, image, image))

#visualizing the image as gray scale because each pixel has three identical values
plt.imshow(img)
plt.show()

#this is a more adequate way to save the images without the axes but I followed the samples 
#plt.imsave("Alaa_Abbas_1.png", img)

#Note that I could have used the libraries for filters but I wanted to show my understanding by making the functions my self
#a function that inverts the image through subtracting values of each pixel from 255
def contrast_inversion(img):
    tmp_img = img
    for i in range(len(tmp_img)):
        for x in range(len(tmp_img[i])):
            for z in range(3):
                tmp_img[i][x][z]= 255-tmp_img[i][x][z]
    return tmp_img


#converting the image
inverted_img = contrast_inversion(img)
#visualizing the image
plt.imshow(inverted_img)
plt.show()

#plt.imsave("Alaa_Abbas_2.png", inverted_img)

#function for making the image into red with some green. I think, for analysis, a blue one would be better, but I wanted to show my understanding
def red_green(img):
    tmp_img = img
    for i in range(len(tmp_img)):
        for x in range(len(tmp_img[i])):
            tmp_img[i][x][0]= 255-tmp_img[i][x][0]
            tmp_img[i][x][1]= 100
            tmp_img[i][x][2]= 0
    return tmp_img

#applying the filter I made
colored = red_green(img)
plt.imshow(colored)
plt.show()

#plt.imsave("Alaa_Abbas_3.png", bluedimg)
