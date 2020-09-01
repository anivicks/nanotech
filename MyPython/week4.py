import random
import numpy as np
from nprime.pyprime import miller_rabin
import json
import math

listFile = []
with open('week4.txt') as f:
    for line in f:
        listFile.append(line.strip())

sqrtProNum = []

range1 = []
for x in range(1, 10001):
    num = format(x, "05")
    num = "1." + num
    range1.append(float(num))

range2 = []
for x in range(10001, 20001):
    num = format(x, "05")
    num = "1." + num
    range2.append(float(num))

range3 = []
for x in range(20001, 30001):
    num = format(x, "05")
    num = "1." + num
    range3.append(float(num))

range4 = []
for x in range(30001, 40001):
    num = format(x, "05")
    num = "1." + num
    range4.append(float(num))

# print(range1)
ranges = [range1, range2, range3, range4]

lineLeast3Array = []

for x in range(1):
    listFileline = (listFile[x]).split(' ')
    firstNum = listFileline[0]
    secondNum = listFileline[1]
    proNum = listFileline[2]

    sqrtpronum = int(math.sqrt(int(proNum)))
    sqrtProNum.append(sqrtpronum)

    proLeast3Array = []

    for y in range(len(ranges)):
        proArr = []
        proArrLeast3 = []
        for z in range(len(ranges[y])):
            pro = sqrtpronum * ranges[y][z]
            pro = int(round(pro))
            proArr.append(pro)

            

        proArr.sort()
        proArrLeast3.append(proArr[0])
        proArrLeast3.append(proArr[1])
        proArrLeast3.append(proArr[2])

        proLeast3Array.append(proArrLeast3)

    lineLeast3Array.append(proLeast3Array)
    # print(proLeast3Array)
    # print(proArrLeast3)

print(lineLeast3Array)

# avgArray = []
# for x in range(4):
#     for y in lineLeast3Array[0][x]:
#         sum = 0
#         for y in range(3):
#             sum = sum + (int(float(lineLeast3Array[0][x][y])))
#     avgArray.append(int(sum/3))

# print(avgArray)