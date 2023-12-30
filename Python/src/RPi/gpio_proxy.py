_rpiLoaded = True

try:
    import RPi.GPIO as GPIO
    print('Loaded RPi.GPIO')
except:
    _rpiLoaded = False
    print('Failed to load RPi.GPIO')

class PWMProxy():
    def start(*args, **kwargs):
        print('start')

    def ChangeDutyCycle(*args, **kwargs):
        print('ChangeDutyCycle')

class GPIOProxy():
    BCM = GPIO.BCM if _rpiLoaded else 'BCM'

    HIGH = GPIO.HIGH if _rpiLoaded else 'HIGH'
    LOW = GPIO.LOW if _rpiLoaded else 'LOW'

    IN = GPIO.IN if _rpiLoaded else 'IN'
    OUT = GPIO.OUT if _rpiLoaded else 'OUT'

    FALLING = GPIO.FALLING if _rpiLoaded else 'FALLING'
    RISING = GPIO.RISING if _rpiLoaded else 'RISING'
    BOTH = GPIO.BOTH if _rpiLoaded else 'BOTH'

    PUD_UP = GPIO.PUD_UP if _rpiLoaded else 'PUD_UP'
    PUD_DOWN = GPIO.PUD_DOWN if _rpiLoaded else 'PUD_DOWN'

    def setmode(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setmode(*args, **kwargs)
        else:
            pass

    def setwarnings(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setwarnings(*args, **kwargs)
        else:
            pass

    def setup(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setup(*args, **kwargs)
        else:
            pass

    def output(*args, **kwargs):
        if _rpiLoaded:
            GPIO.output(*args, **kwargs)
        else:
            pass

    def add_event_detect(*args, **kwargs):
        if _rpiLoaded:
            GPIO.add_event_detect(*args, **kwargs)
        else:
            pass

    def PWM(*args, **kwargs):
        if _rpiLoaded:
            return GPIO.PWM(*args, **kwargs)
        else:
            return PWMProxy()