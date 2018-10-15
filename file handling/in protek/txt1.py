with open("merged.txt", "w") as file:
    for i in range(1,4):
        with open("txt"+str(i)+".txt","r" ) as ab:
            file.write(ab.read())
