import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)

def getMoisture():
    data = ser.readline()
    if data:
        return {
          "value": data.rstrip()
        }
    else:
        return {
          "error": "No moisture data found!"
        }