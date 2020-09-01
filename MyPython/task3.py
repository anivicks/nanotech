import random

n = random.randint(1000000000, 2000000000)
# n = 3456789276827
n = ([int(d) for d in str(n)])
lastDigit = (n[len(n) - 1])
if lastDigit % 2 != 0 and lastDigit != 0 and lastDigit != 5:
   print(lastDigit, ' correct')
else:
    print(lastDigit, ' incorrect')