from machine import ADC, Pin
from utime import sleep

conversion_factor = 3.3 / 65535
increment = 3.3 / 4
potentiometer = ADC(26)
led_blue = Pin(15, Pin.OUT)
led_green = Pin(14, Pin.OUT)
led_orange = Pin(13, Pin.OUT)

while True:
    voltage = potentiometer.read_u16() * conversion_factor
#     print(voltage)
    if voltage < increment:
        led_blue.value(0)
        led_green.value(0)
        led_orange.value(0)
    elif voltage < increment * 2:
        led_blue.value(1)
        led_green.value(0)
        led_orange.value(0)
    elif voltage < increment * 3:
        led_blue.value(1)
        led_green.value(1)
        led_orange.value(0)
    elif voltage < increment * 4:
        led_blue.value(1)
        led_green.value(1)
        led_orange.value(1)
    sleep(.02)
