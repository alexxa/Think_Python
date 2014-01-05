#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.8.1

# Write a function called has_duplicates that takes a list and 
# returns True if there is any element that appears more than 
# once. It should not modify the original list.

def has_duplicates(listik):
    for i in listik:
        if listik.count(i)> 1:
            return True
    return False

print(has_duplicates([1, 2, 3, 2, 4]))
print(has_duplicates([1, 2, 3, 0, 4]))
#END