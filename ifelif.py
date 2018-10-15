def choose(a):
    if a>0 and a<=23:
        if a>4 and a<12:
            print("Good morning")
        elif a >12 and a<16:
            print("good afternoon")
        elif a>16 and a<20:
            print("good evening")
        elif a>20 or a in range(0,4):
            print("good night")
        else:
            print("wrongtime")
    else:
        print("wrongtime")

a = int(input())
choose(a)
