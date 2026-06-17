#from machine import Pin
import time

motion = False
'''
def detection(pin):
    global motion
    motion = True

red = Pin(14, Pin.OUT)
red.off()
sensor = Pin(12, Pin.IN)
sensor.irq(trigger=Pin.IRQ_RISING, handler=detection)

while True:
    if motion:
        red.on()
    time.sleep(2)
    red.off()
    #global motion
    motion = False'''