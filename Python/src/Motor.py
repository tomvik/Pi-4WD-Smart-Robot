from time import sleep

from RPI.gpio_proxy import *
GPIO = GPIOProxy()

KPIN1 = 20
KPIN2 = 21
KPWM1 = 16

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(KPIN1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(KPIN2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(KPWM1, GPIO.OUT, initial = GPIO.HIGH)

pwm_ENA = GPIO.PWM(KPWM1, 2000)
pwm_ENA.start(0)

GPIO.output(KPIN1, GPIO.HIGH)
GPIO.output(KPIN2, GPIO.LOW)
pwm_ENA.ChangeDutyCycle(50)
sleep(2)
GPIO.output(KPIN1, GPIO.LOW)
GPIO.output(KPIN2, GPIO.LOW)
pwm_ENA.ChangeDutyCycle(0)
sleep(2)
GPIO.output(KPIN1, GPIO.LOW)
GPIO.output(KPIN2, GPIO.HIGH)
pwm_ENA.ChangeDutyCycle(50)
sleep(2)
GPIO.output(KPIN1, GPIO.LOW)
GPIO.output(KPIN2, GPIO.LOW)
pwm_ENA.ChangeDutyCycle(0)
