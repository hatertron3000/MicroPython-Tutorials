from machine import Pin
from utime import sleep_ms , sleep

sensor_pir1 = Pin(28, Pin.IN, Pin.PULL_DOWN)
sensor_pir2 = Pin(22, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)

def pir_handler(pin):
    sleep_ms(100)
    if pin.value():
        if pin == sensor_pir1:
            print("ALARM! Motion detected on first sensor!")
            for i in range(50):
                led.toggle()
                buzzer.toggle()
                sleep_ms(100)
        if pin == sensor_pir2:
            print("ALARM! Motion detected on second sensor!")
            for i in range(76):
                led.toggle()
                buzzer.toggle()
                sleep_ms(66)
    
sensor_pir1.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)
sensor_pir2.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    sleep(5)   
