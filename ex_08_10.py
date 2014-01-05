#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.10

# A string slice can take a third index that specifies 
# the step size; that is, the number of spaces between 
# successive characters. A step size of 2 means every other 
# character; 3 means every third, etc.
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the 
# slice [::-1] generates a reversed string. 

# Use this idiom to write a one-line version of is_palindrome 
# from Exercise 6.6.

def is_palindrome(string):
    string = str(string)    #one more line allows to check integers
    return string == string[::-1]

print(is_palindrome('worw'))
print(is_palindrome('woow'))
print(is_palindrome('irina'))
print(is_palindrome('redivider'))
print(is_palindrome('rediveder'))
print(is_palindrome('noon'))
print(is_palindrome('no'))
print(is_palindrome(42))
print(is_palindrome(424))
#END