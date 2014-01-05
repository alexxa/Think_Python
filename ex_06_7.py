#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 6. Fruitful functions

# Exercise 6.7
# A number, a, is a power of b if it is divisible by b and 
# a/b is a power of b. Write a function called is_power that
# takes parameters a and b and returns True if a is a power 
# of b. Note: you will have to think about the base case.

def is_power(a, b):
    if a < b: 
        return False 
    if a == b:  
        return True  
    else:
        return is_power(a / b, b) 
    
print(is_power(1,3))
print(is_power(2,2))
print(is_power(8,2))
print(is_power(9,3))
print(is_power(3,2))
print(is_power(12,2))


#END