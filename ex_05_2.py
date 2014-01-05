#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 5. Conditionals and recursion

# Exercise 5.2
#Write a function called do_n that takes a function object 
# and a number, n, as arguments, and that calls the given 
# function n times.

def do_n(f, n):
    if n <= 0:
        return
    else:
        print(f)
        do_n(f, n-1)
        
do_n('Hello!', 5)

#END