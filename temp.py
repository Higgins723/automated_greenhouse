import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 22

def getTemp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        data = {
            'temp': '{0:0.1f}'.format(temperature),
            'hmd': '{0:0.1f}'.format(humidity)
        }
        return data
    else:
        return 'Failed to get reading. Try again!'
