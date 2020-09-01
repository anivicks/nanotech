import random
import numpy as np
from nprime.pyprime import miller_rabin

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
  # print('The prime numbers are ', onebin, ' ', twobin)
  # print('Their composite product is ', proNum)

  # Convert proNum to binary
  proNum1 = "{0:b}".format(proNum)
  
  # if len(proNum1) < 62:
  #   proNum1 = '0' + proNum1

  onebin1 = "{0:b}".format(onebin)
  twobin1 = "{0:b}".format(twobin)
  onebin2 = int(onebin1)
  twobin2 = int(twobin1)

  # onebinstr = str(onebin1)
  # twobinstr = str(twobin1)

  # print() #print an empty line
  # print('IN BINARY:')
  # print('The prime numbers are ', onebin2, ' ', twobin2, ' ', len(onebin1))
  # # proNumStr = str(proNum1)

  # print('Their composite product is ', proNum1, ' ', len(proNum1))
  results = [proNum1, onebin2, twobin2]
  return results

getBinaryValues = getBinary()

# Collect the binary values and their product
proNum1 = getBinaryValues[0]
firstBinary = str(getBinaryValues[1])
secondBinary = str(getBinaryValues[2])

# To perform XOR on proNum1
def XOR():
  XorArr = []
  for x in range(0, len(proNum1) - 1, 2):
    xor = np.bitwise_xor(int(proNum1[x]), int(proNum1[x+1]))

    XorArr.append(str(xor))

  XorArr = ''.join(XorArr)
  return XorArr
  # print(XorArr, ' ', len(XorArr))

xor1 = XOR()

if len(xor1) < 31:
  xor1 = '0' + xor1

# print(xor1[0], ' ', len(xor1))
# print(xor1, ' ', firstBinary, ' ', secondBinary)

def checkRelation():
  firstMatchTimes = 0
  secondMatchTimes = 0
  for x in range(len(xor1) - 1):
    if xor1[x] == firstBinary[x]:
      # print(xor1[x], ' ', firstBinary[x])
      firstMatchTimes = firstMatchTimes + 1

    if xor1[x] == secondBinary[x]:
      # print(xor1[x], ' ', firstBinary[x])
      secondMatchTimes = secondMatchTimes + 1

  percent1 = str(int((firstMatchTimes / len(xor1)) * 100)) + '%'
  percent2 = str(int((secondMatchTimes / len(xor1)) * 100)) + '%'

  return percent1, percent2

print(checkRelation())

# checkRelation()

# def half():
#   halfProLen = int(len(proNum1) / 2)
#   count = 0
#   copyArr = []
#   for x in proNum1:
#     copyArr.append(x)
#     count += 1
#     if count == halfProLen:
#       print(len(copyArr))
#       break
#   copyArr = ''.join(copyArr)
#   print(copyArr)
  
# half()