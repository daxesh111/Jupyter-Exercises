temperaturesar=[10,20,-40,-274]

def writer(temperatures):
    with open("ctof.txt", 'w') as file:
        for i in temperaturesar:
            if i>-273.15:
                f = 9/5 * i +32
                file.write(str(f)+'\n')

writer(temperaturesar)
