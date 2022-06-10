from machine import Pin, I2C, ADC
from utime import sleep


sda=Pin(16)
scl=Pin(17)
i2c=I2C(0, sda=sda, scl=scl, freq=400000)

thermometer = ADC(4)
conversion_factor = 3.3 / 65535

while True:
    reading = thermometer.read_u16() * conversion_factor
    temperatureC = 25 - (reading - 0.706)/0.001721
    temperatureF = (temperatureC * (9/5)) + 32
    i2c.writeto(114, '\x7C')
    i2c.writeto(114, '\x2D')
    i2c.writeto(114, 'Temp: ' + "%.2f" % temperatureC + ' C')
    i2c.writeto(114, '\x14')
    i2c.writeto(114, '\x14')
    i2c.writeto(114, '\x14')
    i2c.writeto(114, 'Temp: ' + "%.2f" % temperatureF + ' F')
    sleep(2)
