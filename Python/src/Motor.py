from time import sleep

from RPI.GPIOProxy import *
GPIO = GPIOProxy(True)

KPIN1 = 20
KPIN2 = 21
KPWM1 = 16
KFREQUENCY = 2000
KBASEPWM = 1

class Motor():
    """Class to instantiate a motor and control its movement.
    """
    def __init__(self, firstPin: int, secondPin: int, pwmPin: int, pwmFrequency: int):
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
        """
        self.firstPin = firstPin
        self.secondPin = secondPin
        self.pwmPin = pwmPin
        self.pwmFrequency = pwmFrequency
        self.initializePins()

    def initializePins(self):
        """Initializes the GPIO pins.
        """
        GPIO.setup(self.firstPin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.secondPin, GPIO.OUT, initial = GPIO.LOW)
        # TODO: Check if GPIO.LOW works as well
        GPIO.setup(self.pwmPin, GPIO.OUT, initial = GPIO.HIGH)
        self.pwm = GPIO.PWM(self.pwmPin, self.pwmFrequency)

    def stopMotor(self):
        """Stops the motor.
        """
        GPIO.output(KPIN1, GPIO.LOW)
        GPIO.output(KPIN2, GPIO.LOW)
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
        if forward:
            GPIO.output(KPIN1, GPIO.HIGH)
            GPIO.output(KPIN2, GPIO.LOW)
        else:
            GPIO.output(KPIN1, GPIO.LOW)
            GPIO.output(KPIN2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(pwm)

    def moveForward(self, pwm: int):
        """Moves motor forward at a certain pwm.

        Parameters
        ----------
        pwm : int
            Speed at which to move the motor.
        """
        self.moveMotor(True, pwm)

    def moveBackward(self, pwm: int):
        """Moves motor backwards at a certain pwm.

        Parameters
        ----------
        pwm : int
            Speed at which to move the motor.
        """
        self.moveMotor(False, pwm)

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    leftMotor = Motor(KPIN1, KPIN2, KPWM1, KFREQUENCY)

    leftMotor.moveForward(KBASEPWM)
    sleep(0.5)
    leftMotor.stopMotor()
    sleep(0.5)
    leftMotor.moveBackward(KBASEPWM)
    sleep(0.5)
    leftMotor.stopMotor()
