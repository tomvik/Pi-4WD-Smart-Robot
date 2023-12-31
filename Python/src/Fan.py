from RPI.GPIOProxy import *
GPIO = GPIOProxy()

class Fan():
    """Class to instantiate a fan and control its movement.
    """

    def __init__(self, pin: int, debug: bool = False):
        """Initializes the fan instance.

        Parameters
        ----------
        pin : int
            Pin of the fan's motor.
        debug: bool
            Whether it will print debugging information.
        """
        # The debugging has to be set here to be modular.
        # Also, if it's overwritten, it will apply the latest one.
        GPIO.debug = debug
        self.name = '{}'.format(pin)
        self.pin = pin
        self.debug = debug
        self.initializePin()

    def initializePin(self):
        """Initializes the GPIO pin.
        """
        GPIO.setup(self.pin, GPIO.OUT, initial = GPIO.HIGH)

    def stopFan(self):
        """Stops the fan's motor.
        """
        if (self.debug):
            print('{}-{}'.format(self.name, self.stopFan.__qualname__))

        GPIO.output(self.pin, GPIO.HIGH)

    def startFan(self):
        """Starts the fan's motor.
        """
        if (self.debug):
            print('{}-{}'.format(self.name, self.startFan.__qualname__))

        GPIO.output(self.pin, GPIO.LOW)
