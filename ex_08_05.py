#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.5

# Encapsulate this code in a function named count, and 
# generalize it so that it accepts the string and the letter 
# as arguments.


def count(word, target):
    count = 0
    for letter in word:
        if letter == target:
            count = count + 1
    print(count)
    
count('banana', 'a')
count('banana', 'n')
count('banana', 'b')
#END