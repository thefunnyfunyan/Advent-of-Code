import sys
import math

def main(argv):
	matrix = createMatrix(1000,1000)
	instructions = readInInstructions(argv[0])
	
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

def interpretInstructions(instruction):
	brokenInstruction = instruction.split(' ')
	return determineOnOrOff(brokenInstruction) + stripOutCoords(brokenInstruction)
	
def determineOnOrOff(brokenInstruction):
	if(brokenInstruction[0] == 'toggle'):
		return [-1]
	elif(brokenInstruction[1] == 'on'):
		return [1]
	else: 
		return [0]
	
def stripOutCoords(brokenInstruction):
	instructionList = [0,0,0,0]
	brokenInstruction = brokenInstruction[2:] if len(brokenInstruction) == 5 else brokenInstruction[1:]
	instructionList[0] = int(brokenInstruction[0].split(',')[0])
	instructionList[1] = int(brokenInstruction[0].split(',')[1])
	instructionList[2] = int(brokenInstruction[2].split(',')[0])
	instructionList[3] = int(brokenInstruction[2].split(',')[1])
	return instructionList
	
def executeInstruction(matrix, instruction):
	for x in range(instruction[1], instruction[3]+1):
		for y in range(instruction[2], instruction[4]+1):
			matrix[x][y] = setLight(matrix[x][y], instruction[0])

def setLight(currentStatus, instruction):
	if(1 == instruction):
		return 1
	if(0 == instruction):
		return 0
	return abs(currentStatus + instruction)
	

if __name__ == "__main__" : 
	main(sys.argv[1:])