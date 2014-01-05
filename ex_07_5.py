#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 7. Iteration

# Exercise 7.5
# The  mathematician Srinivasa Ramanujan found an infinite series
# that can be used to generate a numerical approximation of pi.
# See page 69 of Think Python

# Write a function called estimate_pi that uses this formula 
# to compute and return an estimate of p. It should use 
# a while loop to compute terms of the summation until the last 
# term is smaller than 1e-15 (which is Python notation for 10^(-15). 
# You can check the result by comparing it to math.pi.

# Solution: http://thinkpython.com/code/pi.py .

from math import sqrt, factorial

def estimate_pi():
    total = 0
    k = 0
    k1 = 2*sqrt(2) / 9801
    while True:
        k2 = factorial(4*k)*(1103+26390*k)
        k3 = factorial(k)**4 * 396**(4*k)
        term = k1 * k2 / k3
        total += term
        if term > 1e-15:
            break
        k += 1
    pi = 1/total
    return pi

print(estimate_pi())
#END