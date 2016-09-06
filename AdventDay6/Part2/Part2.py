import sys

def main(arv):
    matrix = createMatrix(1000, 1000)
    print("Matrix Created")
    fileInstructions = readInInstructions(arv[0])
    print('Instructions Read')
    for individualInstruction in fileInstructions:
        executeInstruction(matrix, interpretInstructions(individualInstruction))
    print(isLit(matrix, 0, 0, 999, 999))

def createMatrix(width, height):
    matrix = [[0 for x in range(width)] for x in range(height)]
    return matrix

def readInInstructions(filePath):
	with open(filePath) as file:
		list = file.readlines()
	stripTrailingNewLine(list)
	return list

def stripTrailingNewLine(list):
	index = 0
	for item in list:
		list[index] = item.strip();
		index += 1

def executeInstruction(matrix, instruction):
    for x in range(instruction[1], instruction[3]+1):
	    for y in range(instruction[2], instruction[4]+1):
		    matrix[x][y] = setLight(matrix[x][y], instruction[0])

def setLight(light, setting):
    if(light == 0 and setting < 0):
        return 0
    return light + setting

def interpretInstructions(instruction):
    brokenInstruction = instruction.split(' ')
    return determineLightChange(brokenInstruction) + stripOutCoords(brokenInstruction)

def stripOutCoords(brokenInstruction):
    instructionList = [0,0,0,0]
    brokenInstruction = brokenInstruction[2:] if len(brokenInstruction) == 5 else brokenInstruction[1:]
    instructionList[0] = int(brokenInstruction[0].split(',')[0])
    instructionList[1] = int(brokenInstruction[0].split(',')[1])
    instructionList[2] = int(brokenInstruction[2].split(',')[0])
    instructionList[3] = int(brokenInstruction[2].split(',')[1])
    return instructionList
	
def determineLightChange(brokenInstruction):
    if(brokenInstruction[0]== 'toggle'):
        return[2]
    if(brokenInstruction[1] == 'on'):
        return [1]
    return [-1]

def isLit(matrix, x1, y1, x2, y2):
    count = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            count += matrix[x][y]

    return count






if __name__ == "__main__":
    main(sys.argv[1:])