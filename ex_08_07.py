#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.7
# There is a string method called count that is similar to 
# the function in the previous exercise. Read the documentation 
# of this method and write an invocation that counts the number 
# of as in 'banana'.
def count(word, target):
    result = word.count(target)
    return result

print(count('banana', 'a'))

#END