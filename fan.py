import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 21
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)

def fanControl(value):
    if value == 'on':
        GPIO.output(pin, GPIO.LOW)
        return {
          "message": "fan was turned on"
        }
    if value == 'off':
        GPIO.output(pin, GPIO.HIGH)
        return {
          "message": "fan was turned off"
        }

    elif value != 'on' and value != 'off':
        return {
            "error": "value must be either 'on' or 'off'"
        }
