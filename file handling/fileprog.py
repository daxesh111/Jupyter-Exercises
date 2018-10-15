file = open("fruits.txt", "r")
content = file.readlines()
print(content)
for i in content:
    print (len(i)-1)
