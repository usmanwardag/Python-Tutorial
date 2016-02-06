
import numpy as np
import cv2

import os

'''
UPDATE:
Install ffmpeg driver.
Work on displaying videos.

'''


from matplotlib import pyplot as plt

def detectPerson():

    path = os.getcwd()+"\Data\video1.avi"
    cap = cv2.VideoCapture(path)

    fgbg = cv2.createBackgroundSubtractorMOG2()

    while(1):
        print "Here"
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    detectPerson()

if __name__ == '__main__':
	main()