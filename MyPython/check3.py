import random
import numpy as np
from nprime.pyprime import miller_rabin
import json
import copy

listFile = []
with open('f6.txt') as f:
    for line in f:
        listFile.append(line.strip())

possibleLastEightArray = []
possibleLastFourArray = []
countForLastFourArray = []

#initiate all the countForLastFourArray items to 0
for x in range(16):
    countForLastFourArray.append(0)

# generate an array of possible last eight digits of proNum
for g in range(256):
    num = "{0:b}".format(g)
    num = format(int(num), "08")
    possibleLastEightArray.append(num)

# generate an array of possible last four digits of inputs
for g in range(16):
    num = "{0:b}".format(g)
    num = format(int(num), "04")
    possibleLastFourArray.append(num)

myCountArray = []

for p in range(len(possibleLastEightArray)):
    for x in range(len(listFile)):
        listFileline = (listFile[x]).split(' ')
        firstNum2 = listFileline[0]
        secondNum2 = listFileline[1]
        proNum = listFileline[2]

        if proNum == possibleLastEightArray[p]:
            for y in range(len(possibleLastFourArray)):
                if firstNum2 == possibleLastFourArray[y]:
                    countForLastFourArray[y] = countForLastFourArray[y] + 1

    # print(countForLastFourArray)
    countLastFourArr = copy.copy(countForLastFourArray)
    myCountArray.append(countLastFourArr)

    # empty the array for the next iteration
    for x in range(len(countForLastFourArray)):
        countForLastFourArray[x] = 0

print(myCountArray)

# totalcountArray2 = []

# for a in range(len(myCountArray)):
#     sum = 0
#     for b in range(len(myCountArray[a])):
#         sum = sum + myCountArray[a][b]

#     totalcountArray2.append(sum)
#     sum = 0

# percentArray = []
# percentArr = []

# for x in range(len(totalcountArray2)):
#     for y in range(len(myCountArray[x])):
#         percent = round(((myCountArray[x][y] / totalcountArray2[x]) * 100), 1)
#         percentArr.append(percent)
#         percent = 0
#     percentArray.append(percentArr)
#     percentArr = []

# # print(len(countArray2))

# print(totalcountArray2)
