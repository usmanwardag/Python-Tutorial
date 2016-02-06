import os
import numpy as np
import cv2

from matplotlib import pyplot as plt

def loadImage():
    path = os.getcwd()+"\Data\image02.jpg"

    #To read in greyscale, provide the second argument as zero.
    image = plt.imread(path)
    return image

def edgeDetection(image):
    edges = cv2.Canny(image,100,125)

    plt.subplot(121),plt.imshow(image)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

def findCorners(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    N = 1000;               # No of best corners to find
    qualityLevel = 0.08     # Quality level is 0-1 and specifies
                            # the threshold below which every
                            # point is ignored.
    minDistance = 8         # Minimum allowable distance between
                            # corners detected.

    corners = cv2.goodFeaturesToTrack(gray,N,qualityLevel,minDistance)

    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        # Create a circle at corner point
        cv2.circle(image,(x,y),3,255,-1)

    plt.imshow(image)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.show()

def main():
    image = loadImage()
    #edgeDetection(image)
    #findCorners(image)


if __name__ == '__main__':
	main()