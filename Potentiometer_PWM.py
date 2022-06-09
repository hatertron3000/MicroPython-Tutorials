from machine import ADC, PWM, Pin
from utime import sleep

conversion_factor = 3.3 / 65535
increment = 3.3 / 4
potentiometer = ADC(26)
led = PWM(Pin(15))

led.freq(1000)

while True:
    reading = potentiometer.read_u16()
    voltage = reading * conversion_factor
    if voltage < .035:
        reading = 0
    print(voltage)                                                                                                         
    sleep(.02)
    led.duty_u16(reading)
