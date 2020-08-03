
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import time
import wiringpi as wp
wp.wiringPiSetupGpio()


def Motor(a,b,pwm):
        wp.pinMode(a,1)
        wp.pinMode(b,1)
        wp.pinMode(pwm,1)
        wp.softPwmCreate(pwm,0,400)
        return a,b,pwm

def dir1(motor,speed):
        (a,b,pwm)=motor
        wp.digitalWrite(a,1)
        wp.digitalWrite(b,0)
        wp.softPwmWrite(pwm,speed)

def dir2(motor,speed):
        (a,b,pwm)=motor
        wp.digitalWrite(a,0)
        wp.digitalWrite(b,1)
        wp.softPwmWrite(pwm,speed)

def forward():
    motor1=Motor(20,16,21)
    motor2=Motor(23,24,25)
    dir1(motor1,90)
    dir1(motor2,100)

def right():
    motor1=Motor(20,16,21)
    motor2=Motor(23,24,25)
    dir1(motor2,100)
    dir2(motor1,90)

def left():
    motor1=Motor(20,16,21)
    motor2=Motor(23,24,25)
    dir1(motor1,90)
    dir2(motor2,100)


def stop():
    motor1=Motor(20,16,21)
    motor2=Motor(23,24,25)
    dir1(motor1,0)
    dir2(motor2,0)

    
greenLower = (0, 130, 41)
greenUpper = (59, 255, 255)
camera = cv2.VideoCapture(0)
ret=camera.set(3,160);
ret=camera.set(4,120);

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

		if radius >10:
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        a=int(x)
			b=int(y)
			r=int(radius)
                        print "x=",a, "y=",b, "z=",r


                        if x>140 and x<200:
                                        forward()


                        elif x<140:
                                        left()

                        elif x>200:
                                        right()

		else:
			stop()
                        print("!!!!!!!!!!!")


#	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()
