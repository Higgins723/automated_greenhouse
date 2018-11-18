import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 20
GPIO.setup(pin, GPIO.OUT)

def pumpControl(value):
    if value == 'on':
        GPIO.output(pin, GPIO.LOW)
        return {
          "message": "pump was turned on"
        }
    if value == 'off':
        GPIO.output(pin, GPIO.HIGH)
        return {
          "message": "pump was turned off"
        }

    elif value != 'on' and value != 'off':
        return {
            "error": "value must be either 'on' or 'off'"
        }
