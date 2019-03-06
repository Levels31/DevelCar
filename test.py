import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(35, gpio.OUT)

gpio.setwarnings(False)

rightWheel = gpio.PWM(12, 50) # GPIO 12 als PWM mit 50Hz
leftWheel = gpio.PWM(35, 50) # GPIO 33 als PWM mit 50Hz

leftWheel.start(50)
rightWheel.start(0)

def rightWheelReverse(speed):
    gpio.output(16, gpio.HIGH)
    gpio.output(18, gpio.LOW)
    rightWheel.ChangeDutyCycle(speed)

def rightWheelForward(speed):
    gpio.output(16, gpio.LOW)
    gpio.output(18, gpio.HIGH)
    rightWheel.ChangeDutyCycle(speed)
    
def leftWheelForward(speed):
    gpio.output(22, gpio.HIGH)
    gpio.output(15, gpio.LOW)
    leftWheel.ChangeDutyCycle(speed)
    
def leftWheelReverse(speed):
    gpio.output(22, gpio.LOW)
    gpio.output(15, gpio.HIGH)
    leftWheel.ChangeDutyCycle(speed)

try:
    while(1):
        rightWheelReverse(0)
except KeyboardInterrupt:
    gpio.cleanup()

