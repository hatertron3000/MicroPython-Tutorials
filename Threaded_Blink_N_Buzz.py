from machine import Pin
from utime import sleep
from random import randrange, random
import _thread

led_gpio15 = Pin(15, Pin.OUT)
led_gpio14 = Pin(14, Pin.OUT)
led_gpio13 = Pin(13, Pin.OUT)
buzzer_gpio12 = Pin(12, Pin.OUT)
global led_index

led_index = 1

def lights_thread():
    global led_index
    while True:
        print(led_index)
        if led_index == 1:
            led_gpio13.value(0)
            led_gpio15.value(1)
            sleep_timer = 5
        elif led_index == 2:
            led_gpio15.value(0)
            led_gpio14.value(1)
            sleep_timer = 3
        elif led_index == 3:
            led_gpio14.value(0)
            led_gpio13.value(1)
            sleep_timer = 1
            
        sleep(sleep_timer)
        
        if led_index != 3:
            led_index+=1
        else:
            led_index = 1
        
_thread.start_new_thread(lights_thread, ())

while True:
    if led_index == 3:
        buzzer_gpio12.value(1)
    else:
        buzzer_gpio12.value(0)

#    led_index = randrange(1,4,1)

#    if led_index == 1:
#        led_gpio15.toggle()
#    if led_index == 2:
#        led_gpio14.toggle()
#    if led_index == 3:
#        led_gpio13.toggle()
    
#   buzzer_gpio12.toggle()
#    sleepTime = random()
#    sleep(sleepTime * .07)
    
    if led_index == 1:
        led_gpio15.value(1)
        sleep_timer = 5
    if led_index == 2:
        led_gpio14.toggle()
    if led_index == 3:
        led_gpio13.toggle()
