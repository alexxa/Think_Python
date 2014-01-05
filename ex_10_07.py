#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.7

# Two words are anagrams if you can rearrange the letters 
# from one to spell the other. Write a function called 
# is_anagram that takes two strings and returns True if they 
# are anagrams.

def is_anagram(listik1, listik2):
    if len(listik1) == len(listik2):
        listik1 = list(listik1)
        listik2 = list(listik2)
        listik1.sort()
        listik2.sort()
        return listik1 == listik2
    else:
        return False
    
print(is_anagram('orchestra','carthorse'))
print(is_anagram('sport','porta'))
print(is_anagram(' ',' ')) # is it ok or not?!
#END