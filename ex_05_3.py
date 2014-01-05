#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 5. Conditionals and recursion

# Exercise 5.3
# Fermats Last Theorem says that there are no integers 
# a, b, and c such that a^n + b^n = c^n for any values of n greater than 2.

# 1. Write a function names check_fermat that takes four parameters a, b, c
# and n and that checks to see if Fermats theorem holds. If n is greater 
# than 2 and it turns out to be true that a^n + b^n = c^n
# the program should print: Holy smokes, Fermat was wrong! Otherwise 
# the program should print: No, that does not work.
 
def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print('Holy Smokes, Fermat was Wrong!')
    else:
        print('No, that doesn\'t work.')
 
check_fermat(3, 4, 5, 3)
print()

# 2. Write a function that prompts the user to input values for a, b, c and n, converts them to
# integers, and uses check_fermat to check whether they violate Fermats theorem.

def fermat():
    a = int(input('Please enter a value for a:\n'))
    b = int(input('Please enter a value for b:\n'))
    c = int(input('Please enter a value for c:\n'))
    n = int(input('Please enter a value for n:\n'))
    check_fermat(a, b, c, n)
    
fermat()

#END