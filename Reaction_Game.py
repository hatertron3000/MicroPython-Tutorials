from machine import Pin
from utime import sleep, ticks_ms, ticks_diff
from urandom import uniform

pressed = False
led = Pin(15, Pin.OUT)
left_button = Pin(14, Pin.IN, Pin.PULL_DOWN)
right_button = Pin(16, Pin.IN, Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    if not pressed:
        pressed=True
        timer_reaction = ticks_diff(ticks_ms(), timer_start)
        print(pin)
        if pin == right_button:
            print("Right player wins!")
        else:
            print("Left player wins!")
        print("Your reaction time was " + str(timer_reaction) + " millseconds!")
        
led.value(1)
sleep(uniform(5, 10))
led.value(0)
timer_start = ticks_ms()
left_button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
