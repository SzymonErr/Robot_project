
#Scan methods
    def scan_input(self):
        return int(input("Input scan result (in cm): "))

    def scan_obstacleMap(self):
        obstacleDetected = False
        blockCounter = 0
        block = 0;
        while(obstacleDetected == False):
            block += 1
            blockCounter += 1
            if self.used_map[self.cords[0]][self.cords[1]] == "_up":
                if self.used_map[self.cords[0]-block][self.cords[1]] == 1.0:
                    obstacleDetected = True
            elif self.used_map[self.cords[0]][self.cords[1]] == "_ri":
                if self.used_map[self.cords[0]][self.cords[1]+block] == 1.0:
                    obstacleDetected = True
            elif self.used_map[self.cords[0]][self.cords[1]] == "_do":
                if self.used_map[self.cords[0]+block][self.cords[1]] == 1.0:
                    obstacleDetected = True
            elif self.used_map[self.cords[0]][self.cords[1]] == "_le":
                if self.used_map[self.cords[0]][self.cords[1]-block] == 1.0:
                    obstacleDetected = True
            else:
                print("Something went wrong, incorrect cords")
        return (blockCounter - 1)