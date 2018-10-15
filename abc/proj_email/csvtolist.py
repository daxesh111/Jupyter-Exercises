
import pandas
import numpy
list1 = []
list2 = []
data = pandas.read_csv("expired_Nov_Dec.csv", header=0, na_filter=False)
data={"Email":list1, "Expiration Date" :list2}

for i in list1:
     if 'gmail' in i:
         print(i)
