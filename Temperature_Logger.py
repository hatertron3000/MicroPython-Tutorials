from machine import ADC
from utime import sleep

sensor_temp = ADC(ADC.CORE_TEMP)

conversion_factor = 3.3 / 65535
file = open("temps.txt", "w")

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperatureC = 27 - (reading - 0.706)/0.001721 # See RP2040 Datasheet and/or Everard & Halfacree "Get Started with MicroPython on Raspberry Pi Pico" pg 99
    temperatureF = (temperatureC * (9/5)) + 32
    
    file.write(str(temperatureC) + "°C/" + str((temperatureC * (9/5)) + 32) + "°F\n")
    file.flush()
    sleep(10)
