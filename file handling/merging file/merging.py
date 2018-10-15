import glob2
import datetime

"""

This file merge the contents of three files given in the folder

Glob 2 stores all filenames in a floder in it's own array

with Open "w" file open a file and write on datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
with open "r" file opena a file and read file in iterative loop one by one

reference = http://strftime.org/
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/5220568?start=0

"""
# this function merges all three file contains

filenames = glob2.glob("*.txt")

def create_file_merge():
        with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
            for i in filenames:
                with open(i,'r') as f:
                    file.write(f.read()+"\n")


create_file_merge()
