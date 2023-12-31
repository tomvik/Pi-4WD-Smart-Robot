from RPI.GPIOProxy import *
GPIO = GPIOProxy()

class Motor():
    """Class to instantiate a motor and control its movement.
    """

    def __init__(self, firstPin: int, secondPin: int, pwmPin: int, pwmFrequency: int, debug: bool = False):
        """Initializes the motor instance.

        Parameters
        ----------
        firstPin : int
            First Pin of the motor.
        secondPin : int
            Second Pin of the motor.
        pwmPin : int
            Pwm Pin of the motor.
        pwmFrequency : int
            pwm frequency of the motor.
        debug: bool
            Whether it will print debugging information.
        """
        # The debugging has to be set here to be modular.
        # Also, if it's overwritten, it will apply the latest one.
        GPIO.debug = debug
        self.name = '{}-{}-{}'.format(firstPin, secondPin, pwmPin)
        self.firstPin = firstPin
        self.secondPin = secondPin
        self.pwmPin = pwmPin
        self.pwmFrequency = pwmFrequency
        self.debug = debug
        self.initializePins()

    def initializePins(self):
        """Initializes the GPIO pins.
        """
        GPIO.setup(self.firstPin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.secondPin, GPIO.OUT, initial = GPIO.LOW)
        # TODO: [Motor] Check if GPIO.LOW works as well.
        GPIO.setup(self.pwmPin, GPIO.OUT, initial = GPIO.HIGH)
        self.pwm = GPIO.PWM(self.pwmPin, self.pwmFrequency)

    def stopMotor(self):
        """Stops the motor.
        """
        if (self.debug):
            print('{}-{}'.format(self.name, self.stopMotor.__qualname__))

        GPIO.output(self.firstPin, GPIO.LOW)
        GPIO.output(self.secondPin, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)

    def moveMotor(self, forward: bool, pwm: int):
        """Moves the motor in a the specified direction and with a certain pwm.

        Parameters
        ----------
        forward : bool
            Whether to move the motor forwards or backwards.
        pwm : int
            Speed at which to move the motor.
        """
        if (self.debug):
            print('{}-{}: {}, {}'.format(self.name, self.moveMotor.__qualname__, forward, pwm))

        if forward:
            GPIO.output(self.firstPin, GPIO.HIGH)
            GPIO.output(self.secondPin, GPIO.LOW)
        else:
            GPIO.output(self.firstPin, GPIO.LOW)
            GPIO.output(self.secondPin, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(pwm)

    def moveForward(self, pwm: int):
        """Moves motor forward at a certain pwm.

        Parameters
        ----------
        pwm : int
            Speed at which to move the motor.
        """
        if (self.debug):
            print('{}-{}: {}'.format(self.name, self.moveForward.__qualname__, pwm))

        self.moveMotor(True, pwm)

    def moveBackward(self, pwm: int):
        """Moves motor backwards at a certain pwm.

        Parameters
        ----------
        pwm : int
            Speed at which to move the motor.
        """
        if (self.debug):
            print('{}-{}: {}'.format(self.name, self.moveBackward.__qualname__, pwm))

        self.moveMotor(False, pwm)
