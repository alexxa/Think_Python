#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 27.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.4

# Write a function named uses_only that takes a word and a string
# of letters, and that returns True if the word contains only 
# letters in the list. 

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True

print(uses_only('banana', 'anb'))
print(uses_only('banana', 'ane'))

#END