#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 11. Dictionaries

# Exercise 11.3

# Dictionaries have a method called keys that returns the keys 
# of the dictionary, in no particular order, as a list.
# Modify print_hist to print the keys and their values in 
# alphabetical order. 

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def print_hist(h):
    listik = sorted(h.keys())
    for i in listik:
        print(i, h[i])
        
h=histogram('brontosaurus')  
print_hist(h)
#END