import time

from fan import fanControl
from pump import pumpControl
from light import lightControl
from data import returnData

# data for plant water level
moistureHigh = 60
moistureLow = 55

temperatureHigh = 75
temperatureLow = 70


def controlLightFan(t):
    if t < temperatureLow:
        lightControl('on')
        fanControl('off')
        print('light on and fan off')
    if t > temperatureHigh:
        lightControl('off')
        fanControl('on')
        print('light off and fan on')

def controlPump(m):
    if m < moistureLow and m != 0:
        pumpControl('on')
        print('pump on')
    if m > moistureHigh:
        pumpControl('off')
        print('pump off')


while True:
    d = returnData()
    print(d)
    temperature = d.get('temperature')
    moisture = d.get('moisture')
    controlLightFan(temperature)
    controlPump(moisture)
    time.sleep(1)