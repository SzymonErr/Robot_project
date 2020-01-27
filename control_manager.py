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
        #createMap("0.0", self.mapName)
        self.map = readMapFromFile(self.mapName)
        self.nav = Navigation2(self.map)
        self.scanner = image_tools()
        self.nav.startNavigation()

    def b_moveForward(self):
        print("b_moveForward")
        self.nav.moveStraight()
        self.robot.forward()

    def b_rotateLeft(self):
        print("b_rotateLeft")
        self.nav.rotateLeft()
        self.robot.left()

    def b_rotateRight(self):
        print("b_rotateRight")
        self.nav.rotateRight()
        self.robot.right()

    def a_firstStepForward(self):
        print("a_firstStepForward")
        self.b_doScan()
        self.b_moveForward()
        self.b_doScan()
        self.b_rotateScannerToRight()
        ran = self.b_doScan()
        printMap(self.nav.used_map)
        return ran

    def a_continueStepForward(self):
        print("a_continueStepForward")
        self.b_moveForward()
        range = self.b_doScan()
        printMap(self.nav.used_map)
        return range

    def a_performForward(self):
        print("a_performForward")
        range = 0
        if(False == self.nav.checkCollision()):
            range = self.a_firstStepForward()
        #range = 0
        right = False
        while(range < 1 and (False == self.nav.checkCollision())):
            a = input("Wait")
            range = self.a_continueStepForward()
            print("1: ", self.nav.checkCollision())
            if (range >= 1):
                right = True
        printMap(self.nav.used_map)
        return right

    def a_performRotate(self, direction_function):
        print("a_performRotate")
        self.b_rotateScannerToMid()
        self.b_doScan()
        direction_function
        printMap(self.nav.used_map)

    def b_doScan(self):
        print("b_doScan")
        printMap(self.nav.used_map)
        #range = self.scanner.analyzeImageAndReturnDist("laser.png")
        #blocks = self.nav.scanRoom(self.nav.scan_arg(range))
        #blocks = self.nav.scanRoom(self.nav.scan_input())
        blocks = self.nav.scanRoom(self.nav.scan_obstacleMap())
        printMap(self.nav.used_map)
        return blocks

    def b_rotateScannerToRight(self):
        print("b_rotateScannerToRight")
        self.servo.max()
        self.nav.faceRobotStraight()
        self.nav.rotateScannerRight()

    def b_rotateScannerToMid(self):
        print("b_rotateScannerToMid")
        self.servo.mid()
        self.nav.faceRobotStraight()

    def a_findNearestWall(self):
        print("a_findNearestWall")
        min_range = 0
        range_min = 100
        min_cord = 0
        for i in range(4):
            min_range = self.b_doScan()
            if(min_range < range_min):
                range_min = min_range
                min_cord = i
            self.b_rotateRight()
        while(min_cord > 0):
            self.b_rotateRight()
            min_cord = min_cord - 1
        printMap(self.nav.used_map)
        print("end of a_findNearestWall")

    def a_rideToNearestWall(self):
        print("a_rideToNearestWall")
        blocks = self.b_doScan()
        for i in range(blocks):
            self.a_continueStepForward()
        self.a_performRotate(self.b_rotateLeft())
        printMap(self.nav.used_map)

    def algorithm(self):
        print("algorithm")
        self.a_findNearestWall()
        self.a_rideToNearestWall()
        i = 0
        while(i < 6):
            if(False == self.a_performForward()):
                self.a_performRotate(self.b_rotateLeft())
            else:
                self.a_performRotate(self.b_rotateRight())
            i += 1

control = controlManager()
control.algorithm()
