import wiringpi as wp

wp.wiringPiSetupGpio()

def Servo(pin):
	wp.pinMode(pin,1)
	wp.softPwmCreate(pin,0,100)
	return pin

def Position(servo,pos):
	(pin)=servo
	wp.softPwmWrite(pin,pos)

def Sweep(servo,delay):
	(pin)=servo
	for i in range(0,20,19):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)
	for i in range(20,0,-19):
		wp.softPwmWrite(pin,i)
		wp.delay(delay)

if __name__=='__main__':
	servo1=Servo(12)
#	Position(servo1,10)
	wp.delay(200)
	Sweep(servo1,1000)
