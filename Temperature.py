from machine import ADC
from utime import sleep

sensor_temp = ADC(4)
conversion_factor = 3.3 / 65535 # 3V3 input voltage / uint size

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperatureC = 27 - (reading - 0.706)/0.001721 # See RP2040 Datasheet and/or Everard & Halfacree "Get Started with MicroPython on Raspberry Pi Pico" pg 99
    # temperatureF = (temperatureC * (9/5)) + 32
    print(str(temperatureC) + "°C/" + str((temperatureC * (9/5)) + 32) + "°F")
    sleep(1)
