#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 7. Iteration

# Exercise 7.

# Write a function named test_square_root that prints a table like this:
# The first column is a number, a; the second column is the square root 
# of a computed with the function from Section 7.5; the third column is 
# the square root computed by math.sqrt; the fourth column is 
# the absolute value of the difference between the two estimates.

from math import sqrt

def test_square_root():
    a = 1
    while a != 10:
        x = a / 2
        while True:
            if x == 0:
                print(a, 'zero')
                break
        
            y = (x + a/x) / 2 
            
            if y == x:
                sqrt_a = sqrt(a)
                diff = abs(sqrt_a - y)
                print(a, '\t', y, '\t', sqrt_a, '\t', diff)
                break
            x = y
        a += 1          
test_square_root()


#END