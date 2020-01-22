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

SAMPLETIME = 0.1

ce0 = Encoder(8)
ce1 = Encoder(7)

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

con = 0

while (ce0.value < 100):
    print("Enc1: ", ce0.encoder.value)
    print("ce0(L): {} ce1(P): {}".format(ce0.value, ce1.value))
    con += 1
    sleep(SAMPLETIME)

print("Finito: ce0(L): {} ce1(P): {}".format(ce0.value, ce1.value))

