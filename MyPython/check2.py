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

for p in range(len(possibleLastFourArray)):
    for x in range(len(listFile)):
        listFileline = (listFile[x]).split(' ')
        firstNum2 = listFileline[0]
        secondNum2 = listFileline[1]
        proNum = listFileline[2]

        if proNum == possibleLastFourArray[p]:
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

    countArr = []
    count00 = 0
    count01 = 0
    count10 = 0
    count11 = 0


totalcountArray2 = []

for a in range(len(countArray)):
    sum = 0
    for b in range(len(countArray[a])):
        sum = sum + countArray[a][b]

    totalcountArray2.append(sum)
    sum = 0

percentArray = []
percentArr = []

for x in range(len(totalcountArray2)):
    for y in range(len(countArray[x])):
        percent = round(((countArray[x][y] / totalcountArray2[x]) * 100), 1)
        percentArr.append(percent)
        percent = 0
    percentArray.append(percentArr)
    percentArr = []

# print(len(countArray2))

# print(totalcountArray2)
print(percentArray)