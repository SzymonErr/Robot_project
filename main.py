from mapReader import *
from mapNavigation import *

cords = list()

my_map = readMapFromFile("map")
#cords = startNavigation(my_map)
printMap(my_map)
print(cords)

nav = Navigation2(my_map)
# nav.startNavigation()
# nav.moveStraight()
# nav.moveStraight()
# nav.rotateLeft()
# nav.moveStraight()
# nav.rotateLeft()
# nav.moveStraight()
# nav.rotateLeft()
# nav.moveStraight()
# nav.rotateRight()
nav.navigationMenu()