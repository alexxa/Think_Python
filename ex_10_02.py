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

# this function works for nested lists of arbitrary depth
def capitalize_nested(nest_list):
	'''Return a new nested list with all strings capitalized.
	   nest_list -> that takes a nested list of strings.'''
	if isinstance(nest_list, list):
		return [capitalize_nested(s) for s in nest_list]
	else:
		return nest_list.capitalize()

print(capitalize_nested(['a','b','c']))
print(capitalize_nested(['a','b','c',['a','a'],['a']]))
print(capitalize_nested([]))
print(capitalize_nested([['banana'],['apple'],['cucumber'],['orange'],['lime'],['tomato']]))
print capitalize_nested(['reporting for cnn', ['watch', 'the', 'news'], ['a boy', 'died', 'in a car fire', ['bug']]])

#END
