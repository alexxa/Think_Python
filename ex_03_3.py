#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 3. Functions

# Exercise 3.3

# Write a function named right_justify that takes a string named s 
# as a parameter and prints the string with enough leading spaces 
# so that the last letter of the string is in column 70 of the display.
# >>> right_justify('allen')
#                                                                 allen

def right_justify(s):
    length = len(s)
    num_of_spaces = 70 - length
    print(' '*num_of_spaces, s)
    
right_justify('allen'*14)
right_justify('allen')

#END