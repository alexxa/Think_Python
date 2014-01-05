#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 7. Iteration

# Exercise 7.1
# Rewrite the function print_n from Section 5.8 using 
# iteration instead of recursion.

def print_n(s, n):
    while n > 0:
        print(s)
        n -= 1
        
print_n(10, 5)
#END