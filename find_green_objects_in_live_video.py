import cv2
import numpy as np


cam = cv2.VideoCapture(0)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

font = cv2.FONT_HERSHEY_SIMPLEX

while (cam.isOpened()):

    ret, img = cam.read()
    if (ret):

        # convert BGR to HSV
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lowerBound = np.array([33, 80, 40])
        upperBound = np.array([102, 255, 255])
        # create the Mask
        mask = cv2.inRange(imgHSV, lowerBound, upperBound)
        # morphology
        maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
        maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

        maskFinal = maskClose
        conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
        for i in range(len(conts)):
            x, y, w, h = cv2.boundingRect(conts[i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img,"Cat",(x,y-10),font,0.55,(0,255,0),1)
        cv2.imshow('maskClose', maskClose)
        cv2.imshow('maskOpen', maskOpen)
        cv2.imshow('mask', mask)
        cv2.imshow('cam', img)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cam.release()
cv2.destroyAllWindows()
