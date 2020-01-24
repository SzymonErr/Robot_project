from gpiozero import DigitalInputDevice, Robot
from time import sleep
from encoder_pid import Encoder

class robotMovement(object):
    def __init__(self):
        self.robot = Robot(left=(12, 13, 6), right=(21, 20, 26))
        self.ce0 = Encoder(8)
        self.ce1 = Encoder(7)
        self.max_speed = 0.4
        self.SAMPLETIME = 0.3
        self.TARGET = 18
        self.KP = 0.06
        self.KI = 0.015
        self.KD = 0.03
        self.forwardTicks = 50
        self.rotateTicks = 15
        self.ce0_sum_error = 0
        self.ce1_sum_error = 0
        self.ce0_sum_count = 0
        self.ce1_sum_count = 0
        self.robot.value = (self.max_speed, self.max_speed)

    def setKI(self, value):
        self.KP = value

    def setKP(self, value):
        self.KI = value

    def setKD(self, value):
        self.KD = value

    def setSAMPLETIME(self, value):
        if (value > 0.0):
            self.SAMPLETIME = value
            print("New value set: " + self.SAMPLETIME)
        else:
            print("Value not changed!")

    def setTARGET(self, value):
        if (value > 0.0):
            self.TARGET = value
            print("New value set: " + self.TARGET)
        else:
            print("Value not changed!")

    def setMaxSpeed(self, value):
        if (value > 0.25 and value <= 1.00):
            self.max_speed = value
            print("New value set: " + self.max_speed)
        else:
            print("Value not changed!")

    def setLeftEncoder(self, pin):
        self.ce0 = Encoder(pin)

    def setRightEncoder(self, pin):
        self.ce1 = Encoder(pin)

    def setRobotValue(self, l_speed, r_speed):
        self.robot.value = (l_speed, r_speed)

    def countGlobalSum(self):
        self.ce0_sum_count += self.ce0.value
        self.ce1_sum_count += self.ce1.value

    def resetEncoders(self):
        self.ce0.reset()
        self.ce1.reset()

    def forward(self):
        print("Driving forward!")
        ce0_prev_error = 0
        ce1_prev_error = 0
        ce0_sum = 0
        ce1_sum = 0
        L_speed = self.max_speed
        R_speed = self.max_speed

        while (ce0_sum < self.forwardTicks and ce1_sum < self.forwardTicks):
            ce0_error = self.TARGET - self.ce0.value
            ce1_error = self.TARGET - self.ce1.value

            R_speed += (ce0_error * self.KP) + (ce0_prev_error * self.KD) + (self.ce0_sum_error * self.KI)
            L_speed += (ce1_error * self.KP) + (ce1_prev_error * self.KD) + (self.ce1_sum_error * self.KI)

            L_speed = max(min(self.max_speed, L_speed), 0)
            R_speed = max(min(self.max_speed, R_speed), 0)
            self.robot.value = (L_speed, R_speed)

            print("ce0(L): {} ce1(P): {}".format(self.ce0.value, self.ce1.value))
            print("L_speed: {} R_speed: {}".format(L_speed, R_speed))

            ce0_sum += self.ce0.value
            ce1_sum += self.ce1.value
            self.countGlobalSum()

            self.resetEncoders()

            sleep(self.SAMPLETIME)

            ce0_prev_error = ce0_error
            ce1_prev_error = ce1_error

            self.ce0_sum_error += ce0_error
            self.ce1_sum_error += ce1_error

        self.setRobotValue(0.0, 0.0)
        self.resetEncoders()

    def left(self):
        print("Driving left!")
        self.resetEncoders()
        while (self.ce0.value < self.rotateTicks and self.ce1.value < self.rotateTicks):
            self.robot.value = (-0.25, 0.25)
        self.setRobotValue(0.0, 0.0)
        self.countGlobalSum()

    def right(self):
        print("Driving right!")
        self.resetEncoders()
        while (self.ce0.value < self.rotateTicks and self.ce1.value < self.rotateTicks):
            self.robot.value = (0.25, -0.25)
        self.setRobotValue(0.0, 0.0)
        self.countGlobalSum()

    def printGlobalTicksValue(self):
        print("Global ticks values: Left encoder: {}  Right encoder: {}".format(self.ce0_sum_count, self.ce1_sum_count))

# robot = robotMovement()
# for i in range(4):
#     robot.forward(100 - i%2*50)
#     sleep(1)
#     robot.left(15)
#     sleep(1)
# #robot.right(100)
# robot.printGlobalTicksValue()
