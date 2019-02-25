import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

p = GPIO.PWM(32, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
        while 1:
                p.ChangeDutyCycle(100)

except KeyboardInterrupt:
        pass
        p.stop()
        GPIO.cleanup()
