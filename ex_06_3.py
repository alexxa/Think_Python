#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 6. Fruitful functions

# Exercise 6.3
# Write a function is_between(x, y, z) that returns True if 
# x <= y <= z or False otherwise.

def is_between(x, y, z):
    if x <= y and y <= z:
        print(True)
    else:
        print(False)

is_between(1, 2, 3)
is_between(2, 3, 1)
is_between(3, 1, 2)

#END