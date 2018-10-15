
import pandas
import numpy
import datetime

comp = datetime.datetime.now()
print(comp)

list1 = []
list2 = []
data = pandas.read_csv("expired_Nov_Dec.csv", header=0, na_filter=False)
list1 = data.Email
list2 = data.Expiration_Date
data={"Email":list1, "Expiration Date" :list2}

"""for i in list1:
     if 'gmail' in i:
         print(i)"""

"""for i in list2:
    if list2[i] < datetime.datetime.now():
        print(i)"""
