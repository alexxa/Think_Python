#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.4

# Write a function called middle that takes a list and returns 
# a new list that contains all but the first and last elements. 
# So middle([1,2,3,4]) should return [2,3].

def middle(listik):
    res = listik[1:len(listik)-1]
    return res

print(middle([1,2,3,4]))
print(middle([1,2,[3,4,5,6],7,8]))
print(middle([1,2,3]))
print(middle([]))
print(middle([1,3]))
#END