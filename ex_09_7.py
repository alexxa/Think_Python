#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 27.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.7
# Give me a word with three consecutive double letters. I'll 
# give you a couple of words that almost qualify, but don't. 
# For example, the word committee, c-o-m-m-i-t-t-e-e. It
# would be great except for the i that sneaks in there. Or 
# Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could take out 
# those i's it would work. But there is a word that has three
# consecutive pairs of letters and to the best of my knowledge 
# this may be the only word. Of course there are probably 500 
# more but I can only think of one. What is the word?

# Write a program to find it. 
# Solution: http://thinkpython.com/code/cartalk1.py

# My solution is faster:
# since if there are three consecutive pairs of letters
# the word can't be shorter then 6 letters. Consequently, if we 
# exclude short words it will speed up the search.

import time

def consecutive(word):
    if word[0] == word[1] and word[2] == word[3]:
        if word[4] == word[5]:
            return word
    return False

def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

             
def author_solution():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)  
            
def my_solution():    
    fin = open('words.txt')   
    for line in fin:
        word = line.strip()
        if len(word) >= 6:
            if is_triple_double(word):
                print(word) 

start_time = time.time()
author_solution()
function_time1 = time.time() - start_time
print()
start_time = time.time()
my_solution()
function_time2 = time.time() - start_time

print('Author solution takes {} s'.format(function_time1)) 
print('My solution takes {} s'.format(function_time2))        
# Author solution takes 0.49902892112731934 s
# My solution takes 0.4690258502960205 s

#END