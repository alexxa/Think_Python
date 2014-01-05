#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 6. Fruitful functions

# Exercise 6.6
# A palindrome is a word that is spelled the same backward and forward, 
# like noon and redivider. Recursively, a word is a palindrome if 
# the first and last letters are the same and the middle is a palindrome.

# 1. Type these functions into a file named palindrome.py and test them out. 
# What happens if you call middle with a string with two letters? One letter? 
# What about the empty string, which is written '' and contains no letters?

word = 'Yo' # no output
# word = 'oo' # no output
# word = 'Y'  # no output
# word = ''   # no output
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

print(middle(word))

print()

# 2. Write a function called is_palindrome that takes a string argument 
# and returns True if it is a palindrome and False otherwise. Remember 
# that you can use the built-in function len to check the length of a string.

# also see ex_08_10 as another solution of the same problem

def is_palindrome(string):
    new_string = str(string)
    if len(new_string) <= 1:
        return(True)
    elif first(new_string) == last(new_string):
        return is_palindrome(middle(new_string))
    else: 
        return(False)  
    
print(is_palindrome('worw'))
print(is_palindrome('woow'))
print(is_palindrome('irina'))
print(is_palindrome('redivider'))
print(is_palindrome('rediveder'))
print(is_palindrome('noon'))
print(is_palindrome('no'))
print(is_palindrome(42))

#END