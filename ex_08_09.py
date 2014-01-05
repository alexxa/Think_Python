#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.8

# Starting with this diagram, execute the program on paper, 
# changing the values of i and j during each iteration. Find 
# and fix the second error in this function.
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1 # the first mistake was defined by author
    
    while j >= 0: # the second mistake was here, it must be >= and not >
        print(i,j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

print(is_reverse('pots', 'stop'))
print()
print(is_reverse('pats', 'stop'))
#END