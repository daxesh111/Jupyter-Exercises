"""
This is a complete code for a dictionary command line interface

You can try this file with HTML to extend the dictionary to use webpage with HTML
"""

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data1  = json.load(open("data.json"))
data2 = data1.keys()

def search(Word1):
    Word1 = Word1.lower()
    if Word1 in data1:
        return data1[Word1]
    elif len(get_close_matches(Word1, data2, cutoff=0.8)) > 0 :
        x = input("Hey did you mean %s instead?" %(get_close_matches(Word1, data2, cutoff=0.8))[0] +" Please Enter Y if yes or N if No : ")
        if x=="y":
            return search(get_close_matches(Word1, data2, cutoff=0.8)[0])
        elif x=="n":
            return ("Word is does not exist")
        else:
            return "You Entered something else than y/n \n"

    else:
        return ("Word is not exist or not goin into function")
        print(Word1)


    '''else:
        for i in data2:
            if Word1.__contains__(i):
                print("did you mean " + i)
                print("Please type yes or no :  y/n ")
                x = input()
                if x=="y":
                    return(search(i))
                else:
                    search(Word1)
                    return ("you have to try again")'''



w = input("enter word to search : ")
out = (search(w))

if type(out) == list:
    if len(out)> 0:
        for i in out:
            print (i)
    else:
        print(out[0])
else:
    print(out)
