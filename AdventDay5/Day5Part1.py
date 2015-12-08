__author__ = 'Brandon'

def naughtyOrNice(listEntry):
    if(vowelChecker(listEntry)):
        if(checkForDouble(listEntry)):
            if(checkForBadCombo(listEntry)):
                return True
    return False

def vowelChecker(listEntry):
    vowelCount = 0
    vowels = 'aeiou'
    for i in listEntry:
        if(i in vowels):
            vowelCount += 1
    return vowelCount >=3

def checkForDouble(listEntry):
    for i in range(0,len(listEntry)-1):
        if(listEntry[i] == listEntry[i+1]):
            return True
    return False

def checkForBadCombo(listEntry):
    if(not 'ab' in listEntry):
        if(not 'cd' in listEntry):
            if(not 'pq' in listEntry):
                if(not 'xy' in listEntry):
                    return True
    return False

def main():
    niceCount = 0
    naughtyNiceList = open('naughtyNiceList.txt')
    for line in naughtyNiceList:
        if(naughtyOrNice(line)):
            niceCount+=1
    print(niceCount)

if __name__ == '__main__': main()

