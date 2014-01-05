#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 27.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.3.1
# Write a function named avoids that takes a word and a string 
# of forbidden letters, and that returns True if the word doesnot 
# use any of the forbidden letters.

def avoids(word, string):
    for letter in word:
        if letter in string:
            return False
    return True

print(avoids('banana', 'ktmu'))
print(avoids('banana', 'ktma'))
print(avoids('banana', 'ktmn'))

#END