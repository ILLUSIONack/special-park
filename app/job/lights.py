from gpiozero import LED
from time import sleep

green   = LED(24)
red     = LED(22)
yellow  = LED(5)

def success():
    green.on()
    sleep(2)
    green.off()

def failure():
    red.on()
    sleep(2)
    red.off()

def loading():
    for i in range(20):
        yellow.on()
        sleep(0.1)
        yellow.off()
        sleep(0.1)

if __name__ == '__main__':
    loading()
    failure()
    success()
