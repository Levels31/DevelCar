import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

leftWheel = GPIO.PWM(23, 50)  # frequency=50Hz
rightWheel = GPIO.PWM(35, 50)

leftWheel.start(0)
rightWheel.start(0)

while(1):
    try:
        leftWheel.ChangeDutyCycle(25)
        rightWheel.ChangeDutyCycle(25)

    except KeyboardInterrupt:
        pass
        leftWheel.stop()
        leftWheel.stop()
        GPIO.cleanup()
        GPIO.cleanup()
