from mapNavigation import *

def algorithm(self):
    continueAlgorithm = True
    counter = 0
    limit = 30
    while (continueAlgorithm == True):
        if (self.checkCollision() == False):
            self.moveStraight()
        else:
            for directions in range(3):
                self.rotateLeft()
                self.scanRoom()
        counter += 1
        if (counter >= limit):
            continueAlgorithm = False
    return