table = [1, 2, 3, 4, 5]
for x in range(1, 11):
    multitable = []
    for y in table:
        pro = x * y
        multitable.append(pro)
    print(multitable)

for x in range(1, 11):
    multitable = []
    multitable.append(x)
    for y in range(4):
        x += multitable[0]
        multitable.append(x)
    print(multitable)