#!/usr/bin/env python3

"""
IMPORTS
"""
#import the necessary package
import imutils
import cv2
import time

"""
FUNCTION DEFINITION
"""

def pre_process(img):
    #convert to gray
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    #blur it
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #threshold it
    _,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)
    return thresh

def contours(thresh_img):
    cnts = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    return cnts

def contour_plot(img):

    thresh_img = pre_process(img) #getting the thresholded image
    cnts = contours(thresh_img) #getting the contours

    #loop over the contours
    for c in cnts:
        #compute the center of contours
        # print("start of the loop")
        M =cv2.moments(c)
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        #
        #draw the contour and center of the shape on the image
        cv2.drawContours(img,[c],-1,(0,255,0),2)
        cv2.circle(img,(cX,cY),7,(255,255,255),-1)
        cv2.putText(img,"center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
        cv2.imshow('output',img)
        # cv2.waitKey(0)

    # cv2.imshow('output',thresh_img)
    cv2.waitKey(0)
    print("reached the end of the program")
    cv2.destroyAllWindows()

"""
MAIN CODE
"""
img = cv2.imread('xxxxx') #path to file
contour_plot(img)
