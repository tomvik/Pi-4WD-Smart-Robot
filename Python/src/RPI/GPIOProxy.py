# TODO: [GPIOProxy] Comment every function in.
import platform

_rpiLoaded = True

if ((platform.system() == 'Linux') and ('rpi' in platform.release())):
    import RPi.GPIO as GPIO # pyright: ignore[reportMissingImports]
    print('Loaded RPi.GPIO successfully!')
else:
    _rpiLoaded = False
    print('This platform does not support RPi.GPIO... Will mock it instead.')

# TODO: Change print order, so the function name goes first.
class PWMProxy():
    def __init__(self, channel, frequency, debug=False):
        self.pwm = GPIO.PWM(channel, frequency) if _rpiLoaded else None
        self.pwmName = '{}_{}'.format(channel, frequency)
        self.debug = debug

    def start(self, dutycycle):
        if (self.debug):
            print('{}-{}: {}'.format(self.pwmName, PWMProxy.start.__qualname__, dutycycle))

        if (self.pwm is not None):
            self.pwm.start(dutycycle)

    def ChangeDutyCycle(self, dutycycle):
        if (self.debug):
            print('{}-{}: {}'.format(self.pwmName, PWMProxy.ChangeDutyCycle.__qualname__, dutycycle))

        if (self.pwm is not None):
            self.pwm.ChangeDutyCycle(dutycycle)

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

    def __new__(cls, debug = False):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GPIOProxy, cls).__new__(cls)
        return cls.instance

    def __init__(self, debug = False):
        self.debug = debug

        if (_rpiLoaded):
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)

    def setmode(self, setMode):
        if (self.debug):
            print('{}: {}'.format(GPIOProxy.setmode.__qualname__, setMode))

        if (_rpiLoaded):
            GPIO.setmode(setMode)

    def setwarnings(self, state):
        if (self.debug):
            print('{}: {}'.format(GPIOProxy.setwarnings.__qualname__, state))

        if (_rpiLoaded):
            GPIO.setwarnings(state)

    def setup(self, channel, direction, pull_up_down = PUD_OFF, initial = None):
        if (self.debug):
            print('{}: {}, {}, {}, {}'.format(GPIOProxy.setup.__qualname__, channel, direction, pull_up_down, initial))

        if (_rpiLoaded):
            GPIO.setup(channel, direction, pull_up_down = pull_up_down, initial = initial)

    def output(self, channel, value):
        if (self.debug):
            print('{}: {}, {}'.format(GPIOProxy.output.__qualname__, channel, value))

        if (_rpiLoaded):
            GPIO.output(channel, value)

    def add_event_detect(self, gpio, edge, callback = None, bouncetime = None):
        if (self.debug):
            print('{}: {}, {}, {}, {}'.format(GPIOProxy.add_event_detect.__qualname__, gpio, edge, callback, bouncetime))

        if (_rpiLoaded):
            GPIO.add_event_detect(gpio, edge, callback = callback, bouncetime = bouncetime)

    def PWM(self, channel, frequency):
        if (self.debug):
            print('{}: {}, {}'.format(GPIOProxy.PWM.__qualname__, channel, frequency))

        return PWMProxy(channel, frequency, self.debug)
