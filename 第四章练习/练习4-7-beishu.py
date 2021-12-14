beishus = list(range(3, 31, 3))
for beishu in beishus:
    print(beishu)

beishus = []
for i in range(3, 31):
    if i % 3 == 0:
        beishus.append(i)
        print(i)
