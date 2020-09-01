import random
import numpy as np
from nprime.pyprime import miller_rabin
import json

firstBinary = ''
secondBinary = ''
xorData = []
firstBinaryArr = []
secondBinaryArr = []
proNum1Arr = []

for x in range(50000):
    numList = []

    def checkPrime():
        count = 0
        while count < 4:
            num = str(random.randint(1000000000, 2000000000))
            last = num[len(num) - 1]
            if int(last) != 0 and int(last) != 5 and int(last) % 2 != 0:
                num = int(num)

                prime = miller_rabin(num, 40)

                if prime:
                    # print(num)
                    # print("YES")
                    numList.append(num)
                    count += 1
                    # else:
                    #   print("NO")

                    # count += 1
                    if count == 2:
                        break

    def getBinary():
        checkPrime()
        # print(numList)
        # print()

        # BASE 10 Operations
        # print('IN BASE 10:')
        onebin = numList[0]
        twobin = numList[1]
        proNum = onebin * twobin

        results = [proNum, onebin, twobin]
        return results

    getBinaryValues = getBinary()

    # Collect the binary values and their product
    proNum1 = str(getBinaryValues[0])
    firstBinary = str(getBinaryValues[1])
    secondBinary = str(getBinaryValues[2])

    firstBinaryArr.append(firstBinary)
    secondBinaryArr.append(secondBinary)
    proNum1Arr.append(proNum1)

# print(percentData, len(percentData))

f = open("week4.txt", "w")
for x in range(len(proNum1Arr)):
    f.write(firstBinaryArr[x] + ' ' + secondBinaryArr[x] + ' ' + proNum1Arr[x] + '\n')
f.close()

# listFile = []
# with open('myFile.txt') as f:
#     for line in f:
#         listFile.append(line.strip())
        
# listFileline = (listFile[0]).split(' ')
# print(listFileline)
# f.writelines(str(percentData))
# for x in range(len(percentData)):
#     f.write(percentData[x])

# f = open("myFile.txt", "r")
# print(f.read())
# f.close()