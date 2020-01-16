from mapNavigation import *

def algorithm(nav):
    continueAlgorithm = True
    counter = 0
    limit = 30
    while (continueAlgorithm == True):
        if (nav.checkCollision() == False):
            nav.moveStraight()
        else:
            for directions in range(3):
                nav.rotateLeft()
                nav.scanRoom()
        counter += 1
        if (counter >= limit):
            continueAlgorithm = False
    return nav

def v2_rotate(nav):
    if (nav.checkCollision() == True):
        nav.rotateLeft()
        nav.faceRobotStraight()
        nav.scanRoom()
        nav.rotateScannerRight()
        return nav

def algorithm_v2(nav):
    continueAlgorithm = True
    counter = 0
    limit = 30
    while (continueAlgorithm == True):
        if (nav.checkCollision() == False):
            nav.moveStraight()
            nav.scanRoom()
        else:
            nav = v2_rotate(nav)
        counter += 1
        if (counter >= limit):
            continueAlgorithm = False
    return nav


