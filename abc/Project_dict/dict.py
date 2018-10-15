import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

"""
This file is for dcitionary app



"""
data  = json.load(open("data.json"))
data1= data.keys()
print(data1)
def trasnlate(word):
    word= word.lower()
    if word in data:
        return data[word]
    else:
        return("The word you entered is not defined in Dictionary")

word1 = input("Enter a word to search : ")
print(trasnlate(word1))
