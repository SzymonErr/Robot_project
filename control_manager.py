from mapNavigation_woRobot import Navigation2
from Moving.encoder_pid import Encoder
from Moving.move import robotMovement
from gpiozero import Servo
from time import sleep
from map_creator import *
from map_reader import *
from bright_decetor import image_tools

'''
#STUBS IMPORT
from stubs.encoder_stub import Encoder
from stubs.robotMovement_stub import robotMovement
from stubs.servo_stub import Servo
'''

class controlManager(object):
    def __init__(self):
        self.robot = robotMovement()
        self.servo = Servo(22)
        self.mapName = "my_map.txt"
        createMap(0.0, self.mapName)
        self.map = readMapFromFile(self.mapName)
        self.nav = Navigation2(self.map)
        self.scanner = image_tools()
        self.nav.startNavigation()

    def b_moveForward(self):
        self.nav.moveStraight()
        self.robot.forward()

    def b_rotateLeft(self):
        self.nav.rotateLeft()
        self.robot.left()

    def b_rotateRight(self):
        self.nav.rotateRight()
        self.robot.right()

    def firstStepForward(self):
        self.b_doScan()
        self.b_moveForward()
        self.b_doScan()
        self.b_rotateScannerToRight()
        self.b_doScan()

    def continueStepForward(self):
        self.b_moveForward()
        self.b_doScan()

    def a_performForward(self):
        self.firstStepForward()
        while(True):
            self.continueStepForward()

    def a_performRotate(self, direction_function):
        self.b_rotateScannerToMid()
        self.b_doScan()
        direction_function

    def b_doScan(self):
        range = self.scanner.analyzeImageAndReturnDist("laser.png")
        blocks = self.nav.scanRoom(self.nav.scan_arg(range))
        return blocks

    def b_rotateScannerToRight(self):
        self.servo.max()
        self.nav.rotateScannerRight()

    def b_rotateScannerToMid(self):
        self.servo.mid()
        self.nav.rotateLeft()

    def a_findNearestWall(self):
        range = 0
        range_min = 100
        min_cord = 0
        for i in range(4):
            range = self.b_doScan()
            if(range < range_min):
                range_min = range
                min_cord = i
            self.b_rotateRight()
        while(min_cord > 0):
            self.b_rotateRight()
            min_cord = min_cord - 1

    def a_rideToNearestWall(self):
        blocks = self.b_doScan()
        for i in range(blocks):
            self.continueStepForward()
        self.a_performRotate(self.b_rotateLeft())

    def algorithm(self):
        self.a_performForward()
        self.a_findNearestWall()
        self.a_rideToNearestWall()

control = controlManager()
control.algorithm()
