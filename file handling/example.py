import datetime

"""

This File creates an empty File with the day
you can use "w to overwrite a new file
or append with a option to enter more text below
reference strftime from http://strftime.org/

"""

filename = "example.txt"
filename1 = datetime.datetime.now()

def create_file():
    """This function creates empy file"""
    with open(filename1.strftime('%b %d')+'.txt',"a") as file:
        file.write("\n This file was updated by Daxesh at " + filename1.strftime('%c') )

create_file()
