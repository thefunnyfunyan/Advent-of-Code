__author__ = 'Brandon'

def breakString(dimensions):
    return dimensions.split("x")

def getSurfaceArea(list):
    firstArea = int(list[0]) * int(list[1])
    secondArea = int(list[0]) * int(list[2])
    thirdArea = int(list[1]) * int(list[2])
    minimum = min([firstArea,secondArea, thirdArea])
    return 2*firstArea + 2*secondArea + 2*thirdArea + minimum

total = 0
file = open("input.txt")
for line in file:
    total += getSurfaceArea(breakString(line))
print(total)


