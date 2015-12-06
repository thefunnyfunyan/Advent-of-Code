__author__ = 'Brandon'

class utilities:
    def __init__(self):
        self.houseList = []
        self.houseCount = 0
        self.xCoord = 0
        self.yCoord = 0

    def findHouseNumberByInstruction(self, dir):
        if(dir == "^"):
            self.yCoord += 1
        elif(dir == ">"):
            self.xCoord += 1
        elif(dir == "<"):
            self.xCoord -=1
        else:
            self.yCoord -=1
        print(str(self.xCoord) + "." + str(self.yCoord))
        return str(self.xCoord) + "." + str(self.yCoord)

    def interpretDrunkenInstructions(self, drunkenInstructions):
        for dir in drunkenInstructions:
            self.addToHouseList(self.findHouseNumberByInstruction(dir))

    def checkHouseList(self, houseNumber):
        try:
            self.houseList.index(houseNumber)
            return True
        except:
            return False
    def addToHouseList(self, houseNumber):
        if(not self.checkHouseList(houseNumber)):
            self.houseList.append(houseNumber)
            self.houseCount +=1

def main():
    file = open("drunkInstruc.txt")
    util = utilities()
    util.interpretDrunkenInstructions(file.read())
    print(util.houseCount)

if __name__ == "__main__": main()








