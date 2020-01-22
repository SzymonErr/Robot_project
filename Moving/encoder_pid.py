from gpiozero import DigitalInputDevice, Robot
from time import sleep

class Encoder(object):
    def __init__(self, pin):
        self._value = 0

        self.encoder = DigitalInputDevice(pin)
        self.encoder.when_activated = self._increment
        #self.encoder.when_deactivated = self._increment
        print("Enc: ", self.encoder.value)

    def reset(self):
        self._value = 0

    def _increment(self):
        self._value += 1

    @property
    def value(self):
        return self._value

SAMPLETIME = 0.2
TARGET = 35
KP = 0.02
KI = 0.005
KD = 0.01

ce0 = Encoder(8)    #LEFT ENCODER
ce1 = Encoder(7)    #RIGHT ENCODER

r = Robot(left=(12, 13, 6), right=(21, 20, 26))

#m = Motor(12,13)
#motor_enable = OutputDevice(5)
#r = AlphaBot()
#r.setPWMA(40)
#r.setPWMB(40)

L_speed = 0.25
R_speed = -0.25
r.value = (L_speed, R_speed)
#r.forward()

ce0_prev_error = 0
ce1_prev_error = 0

ce0_sum_error = 0
ce1_sum_error = 0

con = 0

while True:

    ce0_error = TARGET - ce0.value
    ce1_error = TARGET - ce1.value

    L_speed += (ce0_error * KP) + (ce0_prev_error * KD) + (ce0_sum_error * KI)
    R_speed += (ce1_error * KP) + (ce1_prev_error * KD) + (ce1_sum_error * KI)

    L_speed = max(min(1, L_speed), 0)
    R_speed = max(min(1, R_speed), 0)
    r.value = (L_speed, R_speed)

    print("ce0(L): {} ce1(P): {}".format(ce0.value, ce1.value))
    print("L_speed: {} R_speed: {}".format(L_speed, R_speed))

    ce0.reset()
    ce1.reset()

    sleep(SAMPLETIME)

    ce0_prev_error = ce0_error
    ce1_prev_error = ce1_error

    ce0_sum_error += ce0_error
    ce1_sum_error += ce1_error

    #print("Enc1: ", ce0.encoder.value)
    #print("ce0(L): {} ce1(P): {}".format(ce0.value, ce1.value))
    #con += 1
    #sleep(SAMPLETIME)

print("Finito: ce0(L): {} ce1(P): {}".format(ce0.value, ce1.value))
print("Finito: L_speed: {} R_speed: {}".format(L_speed, R_speed))


