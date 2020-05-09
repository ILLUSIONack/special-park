from gpiozero import LED
from time import sleep

green   = LED(24)
red     = LED(22)
yellow  = LED(5)

def success():
    green.on()
    sleep(2.5)
    green.off()

def failure():
    red.on()
    sleep(2.5)
    red.off()

def loading():
    for i in range(10):
        green.on()
        yellow.on()
        red.on()
        print('LED on')
        sleep(0.1)
        green.off()
        yellow.off()
        red.off()
        print('LED off')
        sleep(0.1)
