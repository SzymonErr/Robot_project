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

def v2_obtuseAngleMovement(nav, range):
    if (range >= Navigation.FIELD_SIZE):
        nav.rotateRight()
        nav. faceRobotStraight()
        nav.rotateScannerRight()
        nav.moveStraight()
    return

def algorithm_v2(nav):
    continueAlgorithm = True
    counter = 0
    limit = 30
    while (continueAlgorithm == True):
        if (nav.checkCollision() == False):
            nav.moveStraight()
            range = nav.scanRoom()
            v2_obtuseAngleMovement(nav, range)
        else:
            nav = v2_rotate(nav)
        counter += 1
        if (counter >= limit):
            continueAlgorithm = False
    return nav


