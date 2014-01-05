#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 6. Fruitful functions

# Exercise 6.2

# Use incremental development to write a function called 
# hypotenuse that returns the length of the hypotenuse of 
# a right triangle given the lengths of the two legs as 
# arguments. Record each stage of the development process as you go.

def hypotenuse(leg1,leg2):
    # stage 1:
    # return 0
    
    # stage 2:
    # leg1_square = leg1**2
    # leg2_square = leg2**2
    # print(leg1_square, leg2_square)
    # return 0
    
    # stage 3:
    # leg1_square = leg1**2
    # leg2_square = leg2**2
    # legs_sum = leg1_square + leg2_square
    # print(legs_sum)
    # return 0
    
    # stage 4:
    # leg1_square = leg1**2
    # leg2_square = leg2**2
    # legs_sum = leg1_square + leg2_square
    # hyp = legs-sum**0.5
    # print(hyp)
    # return 0
    
    # stage 5:
    hyp = (leg1**2 + leg2**2)**0.5
    return hyp

print('{0:.2f}'.format(hypotenuse(1,2)))
#END