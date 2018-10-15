s1 = str(input())
s1 = list(s1)
d = {}
for i in s1:
    if i in d.keys():
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
