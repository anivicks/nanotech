import random
import numpy as np
from nprime.pyprime import miller_rabin
import json
import math
import copy
import matplotlib.pyplot as plt
from scipy import interpolate
from sklearn.ensemble import RandomForestClassifier

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
    proNum = int(listFileline[2])

    sqrtpronum = int(math.sqrt(int(proNum)))
    sqrtProNum.append(sqrtpronum)

    proLeast3Array = []
    modLeast3Array = []

    for y in range(len(ranges)):
        proArr = []
        modArr = []
        proArrLeast3 = []
        modArrLeast3 = []
        for z in range(len(ranges[y])):
            pro = sqrtpronum * ranges[y][z]
            pro = int(round(pro))
            proArr.append(pro)

            modd = proNum % pro
            modArr.append(modd)

        # proArr.sort()
        # proArrLeast3.append(proArr[0])
        # proArrLeast3.append(proArr[1])
        # proArrLeast3.append(proArr[2])

        proMod = {}
        for g in range(len(modArr)):
            proMod[str(modArr[g])] = proArr[g]

        proArrr = copy.copy(proArr)
        modArrr = copy.copy(modArr)

        # for p in range(3):
        #     least = 0
        #     least = min(proArrr)
        #     proArrLeast3.append(least)
        #     proArrr.remove(least)

        for m in range(3):
            leastmod = 0
            leastmod = min(modArrr)
            modArrLeast3.append(leastmod)
            modArrr.remove(leastmod)

        for t in range(3):
            proArrLeast3.append(proMod[str(modArrLeast3[t])])

        proLeast3Array.append(proArrLeast3)
        # modLeast3Array.append(modArrLeast3)

    lineLeast3Array.append(proLeast3Array)
    # print(proLeast3Array)
    # print(proArrLeast3)

# print(proLeast3Array)

avgArray = []
for x in range(4):
    for y in lineLeast3Array[0][x]:
        sum = 0
        for y in range(3):
            sum = sum + (int(float(lineLeast3Array[0][x][y])))
    avgArray.append(int(sum/3))

# print(avgArray)

diffArray = []
for x in range(3):
    diffArray.append(avgArray[x+1] - avgArray[x])

diffArr = np.array(diffArray)

# print(diffArray)

fitArray = []

for x in range(4):
    for y in range(3):
        fitArray.append(proLeast3Array[x][y])

fitArray.append(firstNum)
fitArray1 = np.array(fitArray)

# clf = RandomForestClassifier(random_state=0)
# X = proLeast3Array
# y = [firstNum]
# clf.fit(X, y)
# RandomForestClassifier(random_state=0)


from sklearn.preprocessing import StandardScaler
X = [fitArray1]
print(StandardScaler().fit(X).transform(X))

# print(clf.predict(X))
# print(clf.predict([[4, 5, 6], [14, 15, 16]]))

# print(fitArray)
# plt.plot(diffArray)
# plt.ylabel('some numbers')
# plt.show()