from map_reader import *
from mapNavigation import *

cords = list()

my_map = readMapFromFile("my_first_map")
#cords = startNavigation(my_map)
printMap(my_map)
print(cords)

nav = Navigation(my_map)
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