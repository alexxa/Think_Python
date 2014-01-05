#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 11. Dictionaries

# Exercise 11.2

# Dictionaries have a method called get that takes a key and 
# a default value. If the key appears in the dictionary, get 
# returns the corresponding value; otherwise it returns 
# the default value. Use get to write histogram more concisely.
# You should be able to eliminate the if statement. 


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

h=histogram('brontosaurus')    
print(h)
#END