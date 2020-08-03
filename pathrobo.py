#program to move the robo in the specified path

import wiringpi as wp
wp.wiringPiSetupGpio()

def Motor(x,y,pwm):
	wp.pinMode(x,1)
	wp.pinMode(y,1)
	wp.pinMode(pwm,1)
	wp.softPwmCreate(pwm,0,500)
	return x,y,pwm

def dir2(motor,speed):
	(x,y,pwm)=motor
	wp.digitalWrite(x,0)
	wp.digitalWrite(y,1)
	wp.softPwmWrite(pwm,speed)

def dir1(motor,speed):
	(x,y,pwm)=motor
	wp.digitalWrite(x,1)
	wp.digitalWrite(y,0)
	wp.softPwmWrite(pwm,speed)


a=0

while a<1:
	motor1=Motor(20,16,21)
	motor2=Motor(23,24,25)
	dir2(motor1,82)
	dir2(motor2,100)
	wp.delay(4000)			#for 60 cm forward
	dir1(motor1,0)
	dir1(motor2,0)
#	wp.delay(1000)			#delay time
#	dir1(motor1,100)
#	dir2(motor2,65)
#	wp.delay(427)			#for 60 degree clockwise turn
#	dir1(motor1,0)
#	dir2(motor2,0)
#	wp.delay(1000)			#delay time
#	dir1(motor1,100)
#	dir1(motor2,65)
#	wp.delay(1399)			#for 30 cm forward
#	dir1(motor1,0)
#	dir1(motor2,0)
#	wp.delay(1000)			#delay time
#	dir1(motor1,100)
#	dir2(motor2,65)
#	wp.delay(1820)			#for rotation towards initial position
#	dir1(motor1,0)
#	dir1(motor2,0)
#	wp.delay(1000)			#delay time
#	dir1(motor1,100)
#	dir1(motor2,65)
#	wp.delay(3265)			#for 70 cm forward towards initial pos
#	dir1(motor1,0)
#	dir2(motor2,0)
#	wp.delay(1000)			#delay time
#	dir1(motor1,100)
#	dir2(motor2,65)
#	wp.delay(1700)			#rotate to align with initial position
#	dir1(motor1,0)
#	dir1(motor2,0)
	a+=1

dir1(motor1,0)
dir1(motor2,0)
