from machine import Pin
from utime import sleep
from random import randrange, random

led_gpio15 = Pin(15, Pin.OUT)
led_gpio14 = Pin(14, Pin.OUT)
led_gpio13 = Pin(13, Pin.OUT)
buzzer_gpio12 = Pin(12, Pin.OUT)

while True:
    led_index = randrange(1,4,1)

    if led_index == 1:
        led_gpio15.toggle()
    if led_index == 2:
        led_gpio14.toggle()
    if led_index == 3:
        led_gpio13.toggle()
    
#   buzzer_gpio12.toggle()
    sleepTime = random()
    sleep(sleepTime * .07)
