temperatures = [10,-20,-289,100]
def ctof(cel):
    if float(cel) < -273.15:
        print("there is no lower temp than this in physics")
    else:
        f = float(cel) * 9/5 + 32
        return f

for i in temperatures:
    print(ctof(i))
