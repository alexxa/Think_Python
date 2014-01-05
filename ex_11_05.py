#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 11. Dictionaries

# Exercise 11.5

# Read the documentation of the dictionary method setdefault
# and use it to write a more concise version of invert_dict. 
# Solution: http://thinkpython.com/code/invert_dict.py.

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def invert_dict(d):
    inverse = dict()
    for k, v in d.items():
            inverse.setdefault(v, []).append(k)
    return inverse



hist = histogram('parrot')
print(invert_dict(hist))


#END