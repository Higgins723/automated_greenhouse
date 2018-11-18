import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 16
GPIO.setup(pin, GPIO.OUT)

def lightControl(value):
    if value == 'on':
        GPIO.output(pin, GPIO.LOW)
        return {
          "message": "light was turned on"
        }
    if value == 'off':
        GPIO.output(pin, GPIO.HIGH)
        return {
          "message": "light was turned off"
        }

    elif value != 'on' and value != 'off':
        return {
            "error": "value must be either 'on' or 'off'"
        }