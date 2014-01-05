#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.1

# Write a function called nested_sum that takes a nested list 
# of integers and add up the elements from all of the nested 
# lists.

def nested_sum(listik):
    total = 0
    for i in listik:
        if type(i) is list:
           i = nested_sum(i)  
        total += i
    return total

print(nested_sum([1,2,3,[4,5],[10]]))
print(nested_sum([]))
print(nested_sum([[1],[2],[3],[4],[5],[10]]))
print(nested_sum([1,2,3,[-4,-5],[10]]))
print(nested_sum([1,2,3,[[-4,[-5]],[10]]]))
#END