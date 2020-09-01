import random
import numpy as np
from nprime.pyprime import miller_rabin
import json

listFile = []
with open('f5.txt') as f:
    for line in f:
        listFile.append(line.strip())

possibleLastFourArray = []

count00 = 0
count01 = 0
count10 = 0
count11 = 0

countArray = []
countArr = []

for g in range(16):
    num = "{0:b}".format(g)
    num = format(int(num), "04")
    possibleLastFourArray.append(num)

for x in range(len(listFile)):
    listFileline = (listFile[x]).split(' ')
    firstNum2 = listFileline[0]
    secondNum2 = listFileline[1]
    proNum = listFileline[2]

    if proNum == possibleLastFourArray[0]:
        if firstNum2 == '00':
            count00 = count00 + 1
        elif firstNum2 == '01':
            count01 = count01 + 1
        elif firstNum2 == '10':
            count10 = count10 + 1
        elif firstNum2 == '11':
            count11 = count11 + 1

countArr.append(count00)
countArr.append(count01)
countArr.append(count10)
countArr.append(count11)

countArray.append(countArr)

print(countArray)