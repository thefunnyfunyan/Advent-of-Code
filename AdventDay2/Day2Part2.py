__author__ = 'Brandon'

def breakString(dimensions):
    tempArray = dimensions.split("x")
    return([int(tempArray[0]),int(tempArray[1]),int(tempArray[2])])

def getRibbonDimension(list):
    bowLength = list[0]*list[1]*list[2]
    list.remove(max(list))
    ribbonLength = (2*list[0]) + (2*list[1]) + bowLength
    return ribbonLength


total = 0
file = open("input.txt")
for line in file:
    total += getRibbonDimension(breakString(line))
print(total)