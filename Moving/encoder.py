from gpiozero import DigitalInputDevice

class Encoder(object):
    def __init__(self, pin):
        self._value = 0
        self.encoder = DigitalInputDevice(pin)
        self.encoder.when_activated = self._increment
        self.encoder.when_deactivated = self._increment
        print("Enc: ", self.encoder.value)

    def reset(self):
        self._value = 0

    #def _increment(self):
        self._value += 1

    @property
    def value(self):
        return self._value

