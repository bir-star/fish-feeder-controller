import RPi.GPIO as GPIO
from time import sleep

SERVO_PIN = 3
FREQUENCY = 50
POSITION_COUNT = 12
ANGLE_STEP = (180 / POSITION_COUNT) - .0
START_ANGLE = 18
DAY = 24 * 60 * 60

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
pwm.start(0)

def set_angle(angle, turn_time):
    duty = float(angle) / 18.0 + 2.0
    print("Angle: %d, DC: %f" % (angle, duty))

    GPIO.output(SERVO_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    sleep(turn_time)

    GPIO.output(SERVO_PIN, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def go_to_start():
    set_angle(0, 1);

def run():
    try:
        go_to_start()
        
        for angle in range(START_ANGLE * 10, 1800, int(ANGLE_STEP * 10)):
            set_angle(angle * 0.1, 0.3)
            #sleep(1)
            sleep(DAY)

        go_to_start()                 

    finally:
        pwm.stop()
        GPIO.cleanup()

run()
