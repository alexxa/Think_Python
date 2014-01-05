#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 6. Fruitful functions

# Exercise 6.5
# See about the Ackermann function, A(m, n), on 
# http://en.wikipedia.org/wiki/Ackermann_ function.
# Write a function named ack that evaluates Ackermanns function. 
# Use your function to evaluate ack(3, 4), which should be 125. 
# What happens for larger values of m and n? 
# Solution: http://thinkpython.com/code/ackermann.py.

# my solution differs

def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))
    else:
        print('Something is wrong maybe')
    
print(ack(3,4))
# print(ack(3000,4000)) # returns error for larger values of m and n
#END