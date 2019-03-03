import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(35, gpio.OUT)

rightWheel = gpio.PWM(12, 50) # GPIO 12 als PWM mit 50Hz
leftWheel = gpio.PWM(35, 50) # GPIO 33 als PWM mit 50Hz

leftWheel.start(0)
rightWheel.start(0)

def rightWheelForward(speed):
    gpio.output(16, True)
    gpio.output(18, False)
    rightWheel.ChangeDutyCycle(speed)

def rightWheelReverse(speed):
    gpio.output(16, False)
    gpio.output(18, True)
    rightWheel.ChangeDutyCycle(speed)
    
def leftWheelForward(speed):
    gpio.output(22, True)
    gpio.output(15, False)
    leftWheel.ChangeDutyCycle(speed)

def leftWheelReverse(speed):
    gpio.output(22, False)
    gpio.output(15, True)
    leftWheel.ChangeDutyCycle(speed)


try:
    while(1):
        rightWheelForward(50)
        leftWheelForward(50)
except KeyboardInterrupt:
    gpio.cleanup()

