from machine import ADC, PWM, Pin
from utime import sleep

conversion_factor = 3.3 / 65535
led = PWM(Pin(15))
sensor_temp = ADC(4)

led.freq(1000)

while True:
    tempReading = sensor_temp.read_u16()
    tempVoltage = tempReading * conversion_factor
    temperatureC = 27 - (tempVoltage - 0.706)/0.001721 # See RP2040 Datasheet and/or Everard & Halfacree "Get Started with MicroPython on Raspberry Pi Pico" pg 99
    print(str(temperatureC) + "°C/" + str((temperatureC * (9/5)) + 32) + "°F")                                                                                                         
    led.duty_u16(tempReading)
