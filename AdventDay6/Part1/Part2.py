import sys

def main(arv):
    matrix = part1.createMatrix(1000, 1000)
    print("Matrix Created")
    fileInstructions = readInInstructions(arv[0])
    print('Instructions Read')
    for individualInstruction in fileInstruction:
        executeInstruction(matrix, interpretInstructions(individualInstruction))

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
    # fill out

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






if __name__ == "__main__":
    main(sys.argv[1:])