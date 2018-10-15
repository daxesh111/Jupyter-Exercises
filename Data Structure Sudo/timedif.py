import random
import time
before = time.time()

alist = [random.randint (1,10) for _ in range(1000)]

print(alist[:10])
print ("start sorting")

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

    
insertionSort(alist)
print (alist[:10])
print ("done sorting")
after = time.time() - before
print ( (after),'sec')
