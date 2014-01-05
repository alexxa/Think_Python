#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 12. Tuples

# Exercise 12.2

# In this example, ties are broken by comparing words, so words
# with the same length appear in reverse alphabetical order. For
# other applications you might want to break ties at random.
# Modify this example so that words with the same length appear
# in random order. 
# Hint: see the random function in the random module. 
# Solution: http://thinkpython.com/code/unstable_sort.py

import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
        
    t.sort(reverse=True)
    res = []
    
    for length, _, word in t:
        res.append(word)
    return res

print(sort_by_length(['banana', 'apple', 'kiwi', 'orange', 'cucumber', 'tomato', 'potato']))
print(sort_by_length(['banana', 'apple', 'kiwi', 'orange', 'cucumber', 'tomato', 'potato']))
#END