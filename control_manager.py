from mapNavigation_woRobot import Navigation2
from Moving.encoder_pid import Encoder
from Moving.move import robotMovement
from time import sleep
from map_creator import *
from map_reader import *
from bright_decetor import image_tools

'''
#STUBS IMPORT
from stubs.encoder_stub import Encoder
from stubs.robotMovement_stub import robotMovement
'''

class controlManager(object):
    def __init__(self):
        self.robot = robotMovement()
        self.mapName = "mapa_20.txt"
        #createMap("0.0", self.mapName)
        self.map = readMapFromFile(self.mapName)
        self.nav = Navigation2(self.map)
        self.scanner = image_tools()
        self.nav.startNavigation()

    def b_moveForward(self):
        print("b_moveForward")
        a = input("WAITING FOR ENTER")
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
        ran = self.a_rotateAndScanToRight()
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
        self.b_doScan()
        if(False == self.nav.checkCollision()):
            range = self.a_firstStepForward()
        #range = 0
        right = False
        while(range < 1 and (False == self.nav.checkCollision())):
            #a = input("Wait")
            range = self.a_continueStepForward()
            print("1: ", self.nav.checkCollision())
            if (range >= 1):
                right = True
        printMap(self.nav.used_map)
        return right

    def a_performRotate(self, direction_function):
        print("a_performRotate")
        self.b_doScan()
        direction_function
        printMap(self.nav.used_map)

    def b_doScan(self):
        print("b_doScan")
        a = input("WAITING FOR ENTER")
        printMap(self.nav.used_map)
        range = self.scanner.analyzeImageAndReturnDist()
        blocks = self.nav.scanRoom(self.nav.scan_arg(range))
        #blocks = self.nav.scanRoom(self.nav.scan_input())
        #blocks = self.nav.scanRoom(self.nav.scan_obstacleMap())
        printMap(self.nav.used_map)
        return blocks

    def a_rotateAndScanToRight(self):
        print("b_rotateAndScanToRight")
        self.b_rotateRight()
        dist = self.b_doScan()
        self.b_rotateLeft()
        return dist

    def a_rotateAndScanToLeft(self):
        print("b_rotateAndScanToLeft")
        self.b_rotateLeft()
        dist = self.b_doScan()
        self.b_rotateRight()
        return dist

    def a_findNearestWall(self):
        print("a_findNearestWall")
        min_range = 0
        nearest_wall = 9999
        min_cord = 0
        for i in range(4):
            min_range = self.b_doScan()
            if(min_range < nearest_wall):
                nearest_wall = min_range
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
        while(i < 10):
            if(False == self.a_performForward()):
                self.a_performRotate(self.b_rotateLeft())
            else:
                self.a_performRotate(self.b_rotateRight())
            i += 1

control = controlManager()
control.algorithm()
