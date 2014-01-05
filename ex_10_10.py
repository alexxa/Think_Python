#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 28.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 10. Lists

# Exercise 10.

# Write a function that reads the file words.txt and builds 
# a list with one element per word. Write two versions of this 
# function, one using the append method and the other using
# the idiom t = t + [x]. Which one takes longer to run? Why?
# Hint: use the time module to measure elapsed time. 
# Solution: http://thinkpython.com/code/wordlist.py .

import time

def build_list1():
    fin = open('words.txt')
    list1 = []
    for line in fin:
        word = line.strip()
        list1.append(word)
    return list1   

def build_list2():
    fin = open('words.txt')
    list2 = []
    for line in fin:
        word = line.strip()
        list2 = list2 + [word]
    return list2        

start_time = time.time()
build_list1()
function_time1 = time.time() - start_time

start_time = time.time()
build_list2()
function_time2 = time.time() - start_time

print(function_time1) 
print(function_time2)
#END