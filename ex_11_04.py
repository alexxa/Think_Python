#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 11. Dictionaries

# Exercise 11.4

# Modify reverse_lookup so that it builds and returns a list 
# of all keys that map to v, or an empty list if there are none. 

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def reverse_lookup(d, v):
    res = []
    for k in d:
        if d[k] == v:
            res.append(k)
    #raise ValueError
    return res

h = histogram('parrot carrot')
print(reverse_lookup(h, 2))
print(reverse_lookup(h, 3))
print(reverse_lookup(h, 1))
#END