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

def data():
    try:
        data = getData()
        if type(data) is dict:
            return data
    except:
        return False

def returnData():
    d = data()
    if d != False and d is not None and d != "":
        return d
    else:
        return returnData()