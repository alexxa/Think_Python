#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 11. Dictionaries

# Exercise 11.6
# Run this version of fibonacci and the original with a range 
# of parameters and compare their run times.

import time

known = {0:0, 1:1}

def fibonacci2(n):
    if n in known:
        return known[n]
    res = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = res
    return res


def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    
start_time = time.time()
fibonacci1(30)
function_time1 = time.time() - start_time

start_time = time.time()
fibonacci2(30)
function_time2 = time.time() - start_time

print(function_time1) 
print(function_time2)

# the original one (function_time1) takes much more time
#END