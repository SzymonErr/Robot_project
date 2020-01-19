from matplotlib import pyplot as plt
from PIL import Image
import numpy as np


def createMapInJPG(table, filename):
    #pixels = ([255.0, 0.0, 128.0, 0.0, 0.0], [0.0, 255.0, 128.0, 0.0, 0.0], [0.0, 0.0, 255.0, 0.0, 0.0], [0.0, 0.0, 128.0, 255.0, 0.0], [0.0, 0.0, 128.0, 0.0, 255.0])

    #array = np.array(pixels, dtype=np.uint8)
    for index in range(len(table)):
        if table[index] == "0.5" or table[index] == "0.0":
            table[index] = 0
        elif  table[index] == "1.0":
            table[index] = 255
        else:
            table[index] = 0

    print("Czy cos 1")
    array = np.asarray(table)
    print("Czy cos 2")
    array = np.array(array, dtype=np.uint8)
    print("Czy cos 3")

    new_image=Image.fromarray(array)
    print("Czy cos 4")
    new_image.save(filename + ".jpg")
    return
