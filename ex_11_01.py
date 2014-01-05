#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 11. Dictionaries

# Exercise 11.1

# Write a function that reads the words in words.txt and stores
# them as keys in a dictionary. It doesn't matter what the values
# are. Then you can use the in operator as a fast way to check 
# whether a string is in the dictionary.

def build_dict():
    dictionary = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        dictionary[word] = len(word)
    return dictionary

def is_in_dictionary(string):
    dictionary = build_dict()
    if string in dictionary:
        return True

print(is_in_dictionary('banana'))
        



#END