import platform

# TODO: Transfer this to a common file, or pass it as a parameter to GPIOProxy
DEBUG = False

_rpiLoaded = True

# TODO: Maybe add this in constructor of GPIOProxy?
if ((platform.system() == 'Linux') and ('rpi' in platform.release())):
    # TODO: Maybe exit instead of crashing?
    import RPi.GPIO as GPIO
    print('Loaded RPi.GPIO successfully!')
else:
    _rpiLoaded = False
    print('This platform does not support RPi.GPIO... Will mock it instead.')

class PWMProxy():
    pwmName = ''
    def __init__(self, channel, frequency):
        self.pwmName = '{}_{}'.format(channel, frequency)

    def start(self, dutycycle):
        if (DEBUG):
            print('{}-{}: {}'.format(self.pwmName, PWMProxy.start.__qualname__, dutycycle))

    def ChangeDutyCycle(self, dutycycle):
        if (DEBUG):
            print('{}-{}: {}'.format(self.pwmName, PWMProxy.ChangeDutyCycle.__qualname__, dutycycle))

class GPIOProxy():
    BCM = GPIO.BCM if _rpiLoaded else 'BCM'

    HIGH = GPIO.HIGH if _rpiLoaded else 'HIGH'
    LOW = GPIO.LOW if _rpiLoaded else 'LOW'

    IN = GPIO.IN if _rpiLoaded else 'IN'
    OUT = GPIO.OUT if _rpiLoaded else 'OUT'

    FALLING = GPIO.FALLING if _rpiLoaded else 'FALLING'
    RISING = GPIO.RISING if _rpiLoaded else 'RISING'
    BOTH = GPIO.BOTH if _rpiLoaded else 'BOTH'

    PUD_OFF = GPIO.PUD_OFF if _rpiLoaded else 'PUD_OFF'
    PUD_UP = GPIO.PUD_UP if _rpiLoaded else 'PUD_UP'
    PUD_DOWN = GPIO.PUD_DOWN if _rpiLoaded else 'PUD_DOWN'

    def setmode(self, setMode):
        if (DEBUG):
            print('{}: {}'.format(GPIOProxy.setmode.__qualname__, setMode))
        if (_rpiLoaded):
            GPIO.setmode(setMode)

    def setwarnings(self, state):
        if (DEBUG):
            print('{}: {}'.format(GPIOProxy.setwarnings.__qualname__, state))
        if (_rpiLoaded):
            GPIO.setwarnings(state)

    def setup(self, channel, direction, pull_up_down = PUD_OFF, initial = None):
        if (DEBUG):
            print('{}: {}, {}, {}, {}'.format(GPIOProxy.setup.__qualname__, channel, direction, pull_up_down, initial))
        if (_rpiLoaded):
            GPIO.setup(channel, direction, pull_up_down = pull_up_down, initial = initial)

    def output(self, channel, value):
        if (DEBUG):
            print('{}: {}, {}'.format(GPIOProxy.output.__qualname__, channel, value))
        if (_rpiLoaded):
            GPIO.output(channel, value)

    def add_event_detect(self, gpio, edge, callback = None, bouncetime = None):
        if (DEBUG):
            print('{}: {}, {}, {}, {}'.format(GPIOProxy.add_event_detect.__qualname__, gpio, edge, callback, bouncetime))
        if (_rpiLoaded):
            GPIO.add_event_detect(gpio, edge, callback = callback, bouncetime = bouncetime)

    def PWM(self, channel, frequency):
        if (DEBUG):
            print('{}: {}, {}'.format(GPIOProxy.PWM.__qualname__, channel, frequency))
        if (_rpiLoaded):
            return GPIO.PWM(channel, frequency)
        else:
            return PWMProxy(channel, frequency)
