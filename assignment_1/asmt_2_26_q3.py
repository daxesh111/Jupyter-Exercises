import random
l1 = []
for i in range(0,1000):
    x = random.randint(1,1000)
    if x%5==0 and x%7 == 0:
        l1.append(x)
        if len(l1)==5:
            print(l1)
            break
