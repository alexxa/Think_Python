#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.6

# Write a function called is_sorted that takes a list as 
# a parameter and returns True if the list is sorted in 
# ascending order and False otherwise. You can assume (as 
# a precondition) that the elements of the list can be 
# compared with the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and 
# is_sorted(['b','a']) should return False.

def is_sorted(listik):
    if sorted(listik) == listik:
        return True
    else:
        return False
    
print(is_sorted([1,2,2])) 
print(is_sorted([1,2,1,2])) 
print(is_sorted([]))
print(is_sorted(['b','a']))

#END