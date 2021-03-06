from mapReader import *
from algorithm import *

class Navigation2(object):

    FIELD_SIZE = 40
    def __init__(self, given_map):
        self.used_map = given_map
        self.cords = list()
        self.scanningDirection = "___"

    def startNavigation(self):
        row = int(input("Input start cords (row): "))
        column = int(input("Input start cords (column): "))
        self.used_map[row][column] = "_up"
        self.scanningDirection = "_up"
        self.cords.append(row)
        self.cords.append(column)
        return

    def checkCollision(self):
        Collision = False
        print("used: ")
        printMap(self.used_map)
        obstacleMap = self.used_map
        print("obstacle: ")
        print("Cords: ", self.cords)
        print("Cords type: ", type(self.cords[0]))
        printMap(obstacleMap)
        if self.used_map[self.cords[0]][self.cords[1]] == "_up":
            if str(obstacleMap[self.cords[0] - 1][self.cords[1]]) == "1.0":
                Collision = True
                self.used_map[self.cords[0] - 1][self.cords[1]] = 1.0
        elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
            if str(obstacleMap[self.cords[0]][self.cords[1] + 1]) == "1.0":
                Collision = True
                self.used_map[self.cords[0]][self.cords[1] + 1] = 1.0
        elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
            if str(obstacleMap[self.cords[0] + 1][self.cords[1]]) == "1.0":
                Collision = True
                self.used_map[self.cords[0] + 1][self.cords[1]] = 1.0
        elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
            if str(obstacleMap[self.cords[0]][self.cords[1] - 1]) == "1.0":
                Collision = True
                self.used_map[self.cords[0]][self.cords[1] - 1] = 1.0
        return Collision

    def moveStraight(self):
        if self.used_map[self.cords[0]][self.cords[1]] == "_up":
            self.used_map[self.cords[0]][self.cords[1]] = 0.0
            self.cords[0] -= 1
            self.used_map[self.cords[0]][self.cords[1]] = "_up"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
            self.used_map[self.cords[0]][self.cords[1]] = 0.0
            self.cords[1] += 1
            self.used_map[self.cords[0]][self.cords[1]] = "_ri"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
            self.used_map[self.cords[0]][self.cords[1]] = 0.0
            self.cords[0] += 1
            self.used_map[self.cords[0]][self.cords[1]] = "_do"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
            self.used_map[self.cords[0]][self.cords[1]] = 0.0
            self.cords[1] -= 1
            self.used_map[self.cords[0]][self.cords[1]] = "_le"
        else:
            print("Something went wrong, incorrect cords")
        return

    def rotateLeft(self):
        self.rotateScannerLeft()
        if self.used_map[self.cords[0]][self.cords[1]] == "_up":
            self.used_map[self.cords[0]][self.cords[1]] = "_le"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
            self.used_map[self.cords[0]][self.cords[1]] = "_up"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
            self.used_map[self.cords[0]][self.cords[1]] = "_ri"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
            self.used_map[self.cords[0]][self.cords[1]] = "_do"
        else:
            print("Something went wrong, incorrect cords")
        return

    def rotateRight(self):
        self.rotateScannerRight()
        if self.used_map[self.cords[0]][self.cords[1]] == "_up":
            self.used_map[self.cords[0]][self.cords[1]] = "_ri"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
            self.used_map[self.cords[0]][self.cords[1]] = "_do"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
            self.used_map[self.cords[0]][self.cords[1]] = "_le"
        elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
            self.used_map[self.cords[0]][self.cords[1]] = "_up"
        else:
            print("Something went wrong, incorrect cords")
        return

#Scanner rotations
    def rotateScannerLeft(self):
        if self.scanningDirection == "_up":
            self.scanningDirection = "_le"
        elif self.scanningDirection == "_le":
            self.scanningDirection = "_do"
        elif self.scanningDirection == "_do":
            self.scanningDirection = "_ri"
        elif self.scanningDirection == "_ri":
            self.scanningDirection = "_up"
        else:
            print("Incorrect scanning direction")
        return

    def rotateScannerRight(self):
        if self.scanningDirection == "_up":
            self.scanningDirection = "_ri"
        elif self.scanningDirection == "_ri":
            self.scanningDirection = "_do"
        elif self.scanningDirection == "_do":
            self.scanningDirection = "_le"
        elif self.scanningDirection == "_le":
            self.scanningDirection = "_up"
        else:
            print("Incorrect scanning direction")
        return

#Scan methods
    def scan_input(self):
        return int(input("Input scan result (in cm): "))

    def scan_arg(self, range):
        return range

    def scan_obstacleMap(self):
        obstacleMap = readMapFromFile("obstacleMap2.txt")
        obstacleDetected = False
        blockCounter = 0
        block = 0
        while(obstacleDetected == False):
            block += 1
            blockCounter += 1

            if self.scanningDirection == "_up":
                if obstacleMap[self.cords[0]-block][self.cords[1]] == "1.0":
                    obstacleDetected = True
            elif self.scanningDirection == "_ri":
                if obstacleMap[self.cords[0]][self.cords[1]+block] == "1.0":
                    obstacleDetected = True
            elif self.scanningDirection == "_do":
                if obstacleMap[self.cords[0]+block][self.cords[1]] == "1.0":
                    obstacleDetected = True
            elif self.scanningDirection == "_le":
                if obstacleMap[self.cords[0]][self.cords[1]-block] == "1.0":
                    obstacleDetected = True
            else:
                print("Something went wrong, incorrect cords")
        print("scan_obstacleMap: ", (blockCounter - 1)*Navigation2.FIELD_SIZE)
        return (blockCounter - 1)*Navigation2.FIELD_SIZE

    def scanRoom(self, function):
        record = function
        blocks = int(record)//Navigation2.FIELD_SIZE
        print("scanRoom: ", blocks)
        for block in range(blocks):
            #print("Block: ", block)
            if self.scanningDirection == "_up":
                self.used_map[self.cords[0]-(block+1)][self.cords[1]] = 0.0
            elif self.scanningDirection == "_ri":
                self.used_map[self.cords[0]][self.cords[1]+(block+1)] = 0.0
            elif self.scanningDirection == "_do":
                self.used_map[self.cords[0]+(block+1)][self.cords[1]] = 0.0
            elif self.scanningDirection == "_le":
                self.used_map[self.cords[0]][self.cords[1]-(block+1)] = 0.0
            else:
                print("Something went wrong, incorrect cords")
        if self.scanningDirection == "_up":
            self.used_map[self.cords[0]-(blocks+1)][self.cords[1]] = 1.0
        elif self.scanningDirection == "_ri":
            self.used_map[self.cords[0]][self.cords[1]+(blocks+1)] = 1.0
        elif self.scanningDirection == "_do":
            self.used_map[self.cords[0]+(blocks+1)][self.cords[1]] = 1.0
        elif self.scanningDirection == "_le":
            self.used_map[self.cords[0]][self.cords[1]-(blocks+1)] = 1.0
        else:
            print("Something went wrong, incorrect cords")
        return blocks

    def printNavigationMenu(self):
        print("Navigation menu:")
        print("1 - Start naviagtion")
        print("2 - Move straight")
        print("3 - Turn left")
        print("4 - Turn right")
        print("5 - Print map")
        print("6 - Print current cords")
        print("7 - Load map")
        print("8 - Scan room")
        print("9 - Run algorithm")
        print("r - Rotate scanner right")
        print("t - Rotate scanner left")
        print("0 - Finish navigation")
        print("help - print this menu")

    def navigationMenu(self):
        self.printNavigationMenu()
        continue_loop = True
        while continue_loop == True:
            option = str(input("What to do?: "))
            if option == "1":
                self.startNavigation()
            elif option == "2":
                if(False == self.checkCollision()):
                    self.moveStraight()
                else:
                    print("Collision! Cannot move straight!")
                printMap(self.used_map)
            elif option == "3":
                self.rotateLeft()
                printMap(self.used_map)
            elif option == "4":
                self.rotateRight()
                printMap(self.used_map)
            elif option == "5":
                printMap(self.used_map)
            elif option == "6":
                print("Cords: ", self.cords)
            elif option == "7":
                filename = input("Input map filename: ")
                self.used_map = readMapFromFile(filename)
            elif option == "8":
                self.scanRoom(self.scan_input())
            elif option == "9":
                self = algorithm_v2(self)
            elif option == "r":
                self.rotateScannerRight()
            elif option == "t":
                self.rotateScannerLeft()
            elif option == "0":
                continue_loop = False
                writeMapToFile("temp", self.used_map)
                print("Navigation closed. Bye!")
            elif option.lower() == "help":
                self.printNavigationMenu()
            writeMapToFile("map2", self.used_map)
        return

    #support function
    def faceRobotStraight(self):
        self.scanningDirection = \
            self.used_map[self.cords[0]][self.cords[1]]
        print("ScanningDirection = ", self.scanningDirection)
        print("MovingDirection = ",
              self.used_map[self.cords[0]][self.cords[1]])

