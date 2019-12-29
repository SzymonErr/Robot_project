def createMap(width, height, custom_value, filename):
    file = open(filename, "w")
    for row in range(height):
        for column in range(width):
            file.write(str(custom_value) + " ")
        file.write("\n")
    file.close()

def inputCheck(text, lowerBorder=-9999, upperBorder=9999):
    value = input(text)
    value = float(value)
    if value < lowerBorder:
        print("Invalid value. Please, input value greater than {}".format(lowerBorder))
        value = inputCheck(text, lowerBorder, upperBorder)
    elif (value > upperBorder):
        print("Invalid value. Please, input value lower than {}".format(upperBorder))
        value = inputCheck(text, lowerBorder, upperBorder)
    return value

def getSize():
    width = int(inputCheck("Input map width: ", 1, 100))
    height = int(inputCheck("Input map height: ", 1, 100))
    print("Width: ", width, "Height: ", height)
    return width, height

width, height = getSize()
value = inputCheck("Input value to fill map: ")
name = input("Input file name: ")
createMap(width, height, value, name)