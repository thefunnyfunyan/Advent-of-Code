__author__ = 'Brandon'

def naughtyOrNice(listEntry):
    if(hasRepeatingPair(listEntry)):
        if(hasRepeatLetterWithSpace(listEntry)):
            return True
    return False

def hasRepeatingPair(listEntry):
    if(len(listEntry)<4):
        return False
    possiblePair = listEntry[0:2]
    restOfEntry = listEntry[2:len(listEntry)]
    if(possiblePair in restOfEntry):
        return True
    else:
        return hasRepeatingPair(listEntry[1:len(listEntry)])

def hasRepeatLetterWithSpace(listEntry):
    index = 0
    while index < len(listEntry)-2:
        if(listEntry[index] == listEntry[index+2]):
            return True
        index+=1
    return False

def main():
    niceCount = 0
    naughtyNiceList = open('naughtyNiceList.txt')
    for line in naughtyNiceList:
        if(naughtyOrNice(line)):
            niceCount+=1
    print(niceCount)

def test():
    testString1 = 'qjhvhtzxzqqjkmpb'
    testString2 = 'xxyxx'
    testString3 = 'uurcxstgmygtbstg'
    testString4 = 'ieodomkazucvgmuy'
    testString5 = 'aaa'
    testString6 = "asqwertyuiopasa"
    listOfTestStrings = [testString1, testString2, testString3, testString4, testString5,testString6]
    print("-----Naughty or Nice Test-----")
    for i in listOfTestStrings:
        print("test string: " + i + " --> naughtyOrNice result: " + str(naughtyOrNice(i)))
    print("-----Repeat Pair Test-----")
    for i in listOfTestStrings:
        print("test string: " + i + " --> hasRepeatPair result: " + str(hasRepeatingPair(i)))
    print("-----Repeat Char Test-----")
    for i in listOfTestStrings:
        print("test string: " + i + " --> hasRepeatChar result: " + str(hasRepeatLetterWithSpace(i)))

#if __name__ == '__main__': test()
if __name__ == '__main__': main()

