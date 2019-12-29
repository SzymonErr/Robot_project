from map_reader import *

class Navigation:
    def __init__(self, given_map):
        self.used_map = given_map
        self.cords = list()

    def startNavigation(self):
        row = int(input("Input start cords (row): "))
        column = int(input("Input start cords (column): "))
        self.used_map[row][column] = "_up"
        #printMap(self.used_map)
        self.cords.append(row)
        self.cords.append(column)
        return

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
        #printMap(self.used_map)
        return

    def rotateLeft(self):
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
        #printMap(self.used_map)
        return

    def rotateRight(self):
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
        #printMap(self.used_map)
        return

    def scanRoom(self):
        record = int(input("Input scan result (in cm): "))
        blocks = int(record)//10
        print(blocks)
        for block in range(blocks):
            print("Block: ", block)
            if self.used_map[self.cords[0]][self.cords[1]] == "_up":
                #self.cords[0] -= 1
                self.used_map[self.cords[0]-(block+1)][self.cords[1]] = 0.0
            elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
                #self.cords[1] += 1
                self.used_map[self.cords[0]][self.cords[1]+(block+1)] = 0.0
            elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
                #self.cords[0] += 1
                self.used_map[self.cords[0]+(block+1)][self.cords[1]] = 0.0
            elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
                #self.cords[1] -= 1
                self.used_map[self.cords[0]][self.cords[1]-(block+1)] = 0.0
            else:
                print("Something went wrong, incorrect cords")
        if self.used_map[self.cords[0]][self.cords[1]] == "_up":
            #self.cords[0] -= 1
            self.used_map[self.cords[0]-(blocks+1)][self.cords[1]] = 1.0
        elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
            #self.cords[1] += 1
            self.used_map[self.cords[0]][self.cords[1]+(blocks+1)] = 1.0
        elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
            #self.cords[0] += 1
            self.used_map[self.cords[0]+(blocks+1)][self.cords[1]] = 1.0
        elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
            #self.cords[1] -= 1
            self.used_map[self.cords[0]][self.cords[1]-(blocks+1)] = 1.0
        else:
            print("Something went wrong, incorrect cords")
        # printMap(self.used_map)
        return

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
                self.moveStraight()
            elif option == "3":
                self.rotateLeft()
            elif option == "4":
                self.rotateRight()
            elif option == "5":
                printMap(self.used_map)
            elif option == "6":
                print("Cords: ", self.cords)
            elif option == "7":
                filename = input("Input map filename: ")
                self.used_map = readMapFromFile(filename)
            elif option == "8":
                self.scanRoom()
            elif option == "0":
                continue_loop = False
                print("Navigation closed. Bye!")
            elif option.lower() == "help":
                self.printNavigationMenu()
            writeMapToFile("map2", self.used_map)
        return