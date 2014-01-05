#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.

# Write a function called remove_duplicates that takes a list 
# and returns a new list with only the unique elements from the 
# original. Hint: they do not have to be in the same order.

def remove_duplicates(listik):
    res = []
    for i in listik:
        if i not in res:
            res.append(i)
    return res

print(remove_duplicates(['l','i','s','t','i','k']))      
print(remove_duplicates([1,1,1,2,0,2])) 
#END