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
        print(i)
        yellow.on()
        sleep(1)
        yellow.off()
