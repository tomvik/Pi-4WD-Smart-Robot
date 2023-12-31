# TODO: [Robot] Comment every function.
from time import sleep

from Fan import Fan
from Motor import Motor
from Pins import *

KFREQUENCY = 2000
KBASEPWM = 25

class Robot():

    def __init__(self, pwmFrequency, debug = False):
        self.debug = debug
        self.pwmFrequency = pwmFrequency
        self.initMotors()
        self.initFan()

    def initMotors(self):
        self.leftMotor = Motor(KPINMOTORLEFT1, KPINMOTORLEFT2, KPWMMOTORLEFT1, self.pwmFrequency, self.debug)
        self.rightMotor = Motor(KPINMOTORRIGHT1, KPINMOTORRIGHT2, KPWMMOTORRIGHT1, self.pwmFrequency, self.debug)

    def initFan(self):
        self.fan = Fan(KPINFAN, self.debug)

    def forward(self, pwm):
        self.leftMotor.moveForward(pwm)
        self.rightMotor.moveForward(pwm)

    def backward(self, pwm):
        self.leftMotor.moveBackward(pwm)
        self.rightMotor.moveBackward(pwm)

    def rotateLeft(self, pwm):
        self.leftMotor.moveBackward(pwm)
        self.rightMotor.moveForward(pwm)

    def rotateRight(self, pwm):
        self.leftMotor.moveForward(pwm)
        self.rightMotor.moveBackward(pwm)

    def stopMotors(self):
        self.leftMotor.stopMotor()
        self.rightMotor.stopMotor()

    def startFan(self):
        self.fan.startFan()

    def stopFan(self):
        self.fan.stopFan()

if __name__ == '__main__':
    robot = Robot(KFREQUENCY, True)
    sleep(10)
    robot.forward(KBASEPWM)
    sleep(1.5)
    robot.stopMotors()
    sleep(0.5)
    robot.backward(KBASEPWM)
    sleep(1.5)
    robot.stopMotors()
    sleep(0.5)
    robot.rotateLeft(KBASEPWM)
    sleep(1.5)
    robot.stopMotors()
    sleep(0.5)
    robot.rotateRight(KBASEPWM)
    sleep(1.5)
    robot.stopMotors()
    robot.startFan()
    sleep(2)
    robot.stopFan()