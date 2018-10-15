import random
l1 = []
for i in range(0,100):
    x = random.randint(100,200)
    if x%2==0:
        l1.append(x)
        if len(l1)==5:
            print(l1)
            break
