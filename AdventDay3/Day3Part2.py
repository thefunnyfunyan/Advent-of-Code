__author__ = 'Brandon'

class giftGiver:
    def __init__(self, name):
        self.name = name
        self.xCoord = 0
        self.yCoord = 0

class utilities:
    def __init__(self):
        self.houseList = ["0.0"]
        self.houseCount = 1

    def findHouseNumberByInstruction(self, dir, giver):
        if(dir == "^"):
            giver.yCoord += 1
        elif(dir == ">"):
            giver.xCoord += 1
        elif(dir == "<"):
            giver.xCoord -=1
        else:
            giver.yCoord -=1
        return str(giver.xCoord) + "." + str(giver.yCoord)

    def interpretDrunkenInstructions(self, drunkenInstructions, listOfGiver):
        index=0
        for dir in drunkenInstructions:
            self.addToHouseList(self.findHouseNumberByInstruction(dir, listOfGiver[index]))
            index +=1
            if(index>(len(listOfGiver)-1)):
                index=0

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
    roboSanta = giftGiver("roboSanta")
    santa = giftGiver("Santa")
    util = utilities()
    file = open("drunkInstruc.txt")
    util.interpretDrunkenInstructions(file.read(), [santa, roboSanta])
    print(util.houseCount)

if __name__ == "__main__": main()

