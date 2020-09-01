import random
import numpy as np

numList = []

def checkPrime():
  count = 0
  while count < 4:
      num = str(random.randint(1000000000, 2000000000))
      last = num[len(num) - 1]
      if int(last) != 0 and int(last) != 5 and int(last) % 2 != 0:

        def miller_rabin(n, k):
            n = int(n)
            r, s = 0, n - 1
            while s % 2 == 0:
                r += 1
                s //= 2
            for _ in range(k):
                a = random.randrange(2, n - 1)
                x = pow(a, s, n)
                if x == 1 or x == n - 1:
                    continue
                for _ in range(r - 1):
                    x = pow(x, 2, n)
                    if x == n - 1:
                        break
                else:
                    return 0
            return 1

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

checkPrime()
print('The two prime numbers are : ', numList)

proNum = int(numList[0]) * int(numList[1])
print('The composite product is: ', proNum)