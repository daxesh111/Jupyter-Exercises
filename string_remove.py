c = ["hi" , 2 , "Daxesh" ]
c.append(c[1])
print(c)

d = c.pop(int("2")) # pop(index)
print(c) # c is left after pop but in pop "Daxesh" saved
print(d) # d is saved with "Daxesh"
c.remove(c[0])
print(c)
type(c[0])
