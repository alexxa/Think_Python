#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 6. Fruitful functions

# Exercise 6.8
# The greatest common divisor (GCD) of a and b is the largest number 
# that divides both of them with no remainder. 
# One way to find the GCD of two numbers is Euclids algorithm, which 
# is based on the observation that if r is the remainder when a is 
# divided by b, then gcd(a, b) = gcd(b, r). As a base case,
# we can use gcd(a, 0) = a.

# Write a function called gcd that takes parameters a and b and returns 
# their greatest common divisor.

def gcd(a, b):
    
    if a >= b and b != 0:
        r = a % b
        if r == 0:
            print(b)
        else:
            return gcd(b, r)
    elif a <= b and a != 0:
        r = b % a
        if r == 0:
            print(a)
        else:
            return gcd(a, r)
    else:
        print('Zero division')

gcd(18, 2)
gcd(2, 18)
gcd(9, 18)
gcd(4,4)
gcd(4,0)
gcd(11, 13)
#END