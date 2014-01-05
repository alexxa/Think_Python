#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.1

# Write a function that takes a string as an argument and 
# displays the letters backward, one per line.

def print_string_backward(string):
    index = len(string)
    while index > 0:
        print(string[index-1])
        index -=1
        
print_string_backward('string')
print()
print_string_backward('Merry Christmas and Happy New Year!')

#END