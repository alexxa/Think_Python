#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 12. Tuples

# Exercise 12.1

# Write a function called sumall that takes any number of 
# arguments and returns their sum.

def sumall(*t):
    return sum(t)

print(sumall(1,2,3,4,5))
#END