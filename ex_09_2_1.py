#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 26.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.2.1

# Write a function called has_no_e that returns True if 
# the given word does not have the letter e in it.

def has_no_e(word):
    word = word.lower()
    for letter in word:
        if letter == 'e':
            return False
    return True

print(has_no_e('test'))
print(has_no_e('etest'))
print(has_no_e('banana'))
print(has_no_e('line'))
print(has_no_e(''))
print(has_no_e(' '))
print(has_no_e(' e'))
#END