#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 7. Iteration

# Exercise 7.2
# Encapsulate this loop in a function called square_root that 
# takes a as a parameter, chooses a reasonable value of x, and 
# returns an estimate of the square root of a.

def square_root(a):
    x = a
    while True:
        if x == 0:
            return 0
        
        y = (x + a/x) / 2        
        if y == x:
            return y
        x = y
            
print(square_root(0))
print(square_root(1))
print(square_root(2))
print(square_root(9))
print(square_root(225))
#END