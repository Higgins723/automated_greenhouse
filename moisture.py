import serial
import json


def getData():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    data = ser.readline()
    if data:
        value = json.loads(data.decode('utf-8').replace("'", '"'))
        return value
    else:
        return {
          "error": "No moisture data found!"
        }