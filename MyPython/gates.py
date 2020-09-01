import random
import numpy as np
from nprime.pyprime import miller_rabin
import json

listFile = []
with open('myFile.txt') as f:
    for line in f:
        listFile.append(line.strip())

def xorGate():
    XorArray = []
    for x in range(len(listFile)):
        listFileline = (listFile[x]).split(' ')
        pronum = listFileline[2]
        XorArr = []
        for y in range(0, len(pronum) - 1, 2):
            xor = np.bitwise_xor(int(pronum[y]), int(pronum[y+1]))
            XorArr.append(str(xor))

        XorArr = ''.join(XorArr)
        XorArray.append(XorArr)
        # print(num1, num2, pronum)
    
    # Check the match percentage
    
    return XorArray

def orGate():
    orGateArray = []
    for x in range(len(listFile)):
        listFileline = (listFile[x]).split(' ')
        pronum = listFileline[2]
        orGateArr = []
        for y in range(0, len(pronum) - 1, 2):
            orGate = np.bitwise_or(int(pronum[y]), int(pronum[y+1]))
            orGateArr.append(str(orGate))

        orGateArr = ''.join(orGateArr)
        orGateArray.append(orGateArr)
        # print(orGateArray)
    return orGateArray

def andGate():
    andGateArray = []
    for x in range(len(listFile)):
        listFileline = (listFile[x]).split(' ')
        pronum = listFileline[2]
        andGateArr = []
        for y in range(0, len(pronum) - 1, 2):
            andGate = np.bitwise_and(int(pronum[y]), int(pronum[y+1]))
            andGateArr.append(str(andGate))

        andGateArr = ''.join(andGateArr)
        andGateArray.append(andGateArr)
        # print(num1, num2, pronum)
    return andGateArray

def combinedGate(orGate, andGate):
    orGate = orGate
    andGate = andGate
    combGateArray = []
    
    for a in range(len(orGate)):
        combGateArr = []
        for b in range(len(orGate[a])):
            combGate = np.bitwise_or(int(orGate[a][b]), int(andGate[a][b]))
            combGateArr.append(str(combGate))
        
        combGateArr = ''.join(combGateArr)
        combGateArray.append(combGateArr)
    # print(len(combGateArray))
    return combGateArray

def forLastFour():
    eightDigitsArray = []
    num1FourArray = []
    num2FourArray = []

    for x in range(len(listFile)):
        eightDigitsArr = []
        num1FourArr = []
        num2FourArr = []

        #get each line from myfile.txt and split to its respective contents
        listFileline = (listFile[x]).split(' ')
        pronum = listFileline[2]
        firstNum = listFileline[0]
        secondNum = listFileline[1]

        # get the last eight digits of pronum
        for y in range(8):
            eightDigitsArr.append(pronum[len(pronum) - 2 - y])

        eightDigitsArr.reverse()
        eightDigitsArr = ''.join(eightDigitsArr)
        eightDigitsArray.append(eightDigitsArr)


        # get last four digits of the two multiplying numbers
        for y in range(4):
            num1FourArr.append(firstNum[len(firstNum) - 2 - y])
            num2FourArr.append(secondNum[len(secondNum) - 2 - y])

        num1FourArr.reverse()
        num2FourArr.reverse()
        num1FourArr = ''.join(num1FourArr)
        num2FourArr = ''.join(num2FourArr)

        num1FourArray.append(num1FourArr)
        num2FourArray.append(num2FourArr)

    f = open("f6.txt", "w")
    for x in range(len(listFile)):
        f.write(num1FourArray[x] + ' ' + num2FourArray[x] + ' ' + eightDigitsArray[x] + '\n')
    f.close()

    # print(eightDigitsArray, num1FourArray, num2FourArray)

    #     andGateArr = []
    #     for y in range(0, len(pronum) - 1, 2):
    #         andGate = np.bitwise_and(int(pronum[y]), int(pronum[y+1]))
    #         andGateArr.append(str(andGate))

    #     andGateArr = ''.join(andGateArr)
    #     andGateArray.append(andGateArr)
    #     # print(num1, num2, pronum)
    # return andGateArray

def checkRelation(gatesArray):
    # fetches the arguments and defines other necessary variables
    gatesArray = gatesArray
    percent1Arr = []
    percent2Arr = []
    # gets the two binary operands for each lines
    for x in range(len(listFile)):
        firstMatchTimes = 0
        secondMatchTimes = 0
        listFileline = (listFile[x]).split(' ')
        firstNum = listFileline[0]
        secondNum = listFileline[1]

        # calculates the match percentage
        for p in range(len(gatesArray[x])):
            if gatesArray[x][p] == firstNum[p]:
                firstMatchTimes = firstMatchTimes + 1

            if gatesArray[x][p] == secondNum[p]:
                secondMatchTimes = secondMatchTimes + 1

        # print(firstNum, secondNum)
        # print(firstMatchTimes, secondMatchTimes)

        percent1 = str(int((firstMatchTimes / len(gatesArray[x])) * 100)) # + '%'
        percent2 = str(int((secondMatchTimes / len(gatesArray[x])) * 100)) # + '%'

        percent1Arr.append(percent1)
        percent2Arr.append(percent2)

    aggPercent1 = 0
    aggPercent2 = 0
    
    for w in range(len(listFile)):
        aggPercent1 += int(percent1Arr[w])
        aggPercent2 += int(percent2Arr[w])
    
    aggPercent1 = aggPercent1 / len(listFile)
    aggPercent2 = aggPercent2 / len(listFile)
    
    return aggPercent1, aggPercent2

# print(checkRelation(combinedGate(orGate(), andGate())))

forLastFour()