def printMap(my_map):
    for row in range(len(my_map)):
        buffer = ""
        for column in range(len(my_map[row])):
            buffer += str(my_map[row][column]) + " "
        print(buffer)
    print("")

def readMapFromFile(filename):
    read_map = list()
    with open(filename, "r") as my_map:
        for rows in my_map:
            sorted_map = rows.strip().split(' ')
            read_map.append(sorted_map)
    return read_map

def writeMapToFile(filename, current_map):
    with open(filename, "w+") as my_map:
        for row in range(len(current_map)):
            buffer = ""
            for column in range(len(current_map[row])):
                buffer += str(current_map[row][column]) + " "
            my_map.write(buffer + '\n')
    return

#my_map = readMapFromFile("my_first_map")
#printMap(my_map)
#my_map[2][3] = 0.0
#printMap(my_map)
#writeMapToFile("mapa_testowa", my_map)
