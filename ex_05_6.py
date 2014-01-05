#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 5. Conditionals and recursion

# Exercise 6.1
# Write a compare function that returns 
# 1 if x > y, 
# 0 if x == y, and 
# -1 if x < y.

def compare(x,y):
    if x > y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
print(compare(1,2))
print(compare(2,1))
print(compare(1,1))

#END