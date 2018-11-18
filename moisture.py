import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)

def getData():
    data = ser.readline()
    if data:
        return json.loads(data.decode('utf-8').replace("'", '"'))
    else:
        return {
          "error": "No moisture data found!"
        }