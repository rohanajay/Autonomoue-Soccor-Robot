
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import time

greenLower = (0, 144, 83)
greenUpper = (255, 255, 255)


#greenLower = (12, 96, 186)
#greenUpper = (179, 255, 255)
#greenLower = (8,100,100)
#greenUpper = (28,255, 255)

camera = cv2.VideoCapture(0)

while True:
	(grabbed, frame) = camera.read()
	frame = imutils.resize(frame, width=320, height=240)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        a=int(x)
			b=int(y)
			r=int(radius)
                        print "x=",a, "y=",b, "z=",r             
              

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()
