#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.6

# Rewrite this function so that instead of traversing 
# the string, it uses the threeparameter version of find 
# from the previous section.

def count(word, target, index):
    word, target = word.lower(), target.lower()
    counter = 0
    while index < len(word):
        if word[index] == target:
            counter = counter + 1
        index = index + 1
    return counter

print(count('banana', 'a', 0))
print(count('baNana', 'N', 0))
print(count('banana', 'b', 0))
print(count('banana', 'b', 2))
print(count('banana', 'a', 2))
#END