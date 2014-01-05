#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.5

# Write a function called chop that takes a list, modifies it 
# by removing the first and last elements, and returns None.

def middle(listik):
    listik = listik[1:len(listik)-1]
    print(listik)
    return 

print(middle([1,2,3,4]))
print(middle([1,2,[3,4,5,6],7,8]))
print(middle([1,2,3]))
print(middle([]))
print(middle([1,3]))

#END