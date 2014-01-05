#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.2

# Use capitalize_all to write a function named capitalize_nested
# that takes a nested list of strings and returns a new nested 
# list with all strings capitalized.

def capitalize_nested(listik):
    capitalized = []
    for i in listik:
        if type(i) is list:
            i = capitalize_nested(i)
        else:
            i = i.capitalize()  
        capitalized.append(i)
    return capitalized

print(capitalize_nested(['a','b','c']))
print(capitalize_nested(['a','b','c',['a','a'],['a']]))
print(capitalize_nested([]))
print(capitalize_nested([['banana'],['apple'],['cucumber'],['orange'],['lime'],['tomato']]))

#END