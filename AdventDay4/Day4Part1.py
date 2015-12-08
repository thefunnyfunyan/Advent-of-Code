__author__ = 'Brandon'
import hashlib


def converter(num):
    totalString = "ckczppom" + str(num)
    return hashlib.md5(bytes(totalString, 'utf-8')).hexdigest()

def check(hexNum):
    goodNum = True
    index = 0
    while (index < 5 and goodNum == True):
        if(hexNum[index] != '0'):
            goodNum = False
        index += 1
    return goodNum


def main():
    foundNum = False
    index = -1
    while(not foundNum):
        index += 1
        foundNum = check(converter(index))
        if(index%100==0):
            print("...")
    print(foundNum)
    print(index)
    print(converter(index))

if(__name__ == "__main__"): main()

print((converter(609043)))

