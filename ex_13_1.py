#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 13. Case study: data structure selection

#STATUS: check for refactoring

# Exercise 13.

# Write a program that reads a file, breaks each line into words, 
# strips whitespace and punctuation from the words, and converts 
# them to lowercase.

# Hint: The string module provides strings named whitespace, which
# contains space, tab, newline, etc., and punctuation which contains
# the punctuation characters. Let's see if we can make Python swear:
# >>> import string
# >>> print string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Also, you might consider using the string methods strip, replace 
# and translate.
import string, time

def del_punctuation(item):
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item 

def break_into_words():
    book = open('tsawyer.txt')
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            #print(item)
            words_list.append(item)
    return words_list


print(break_into_words())

start_time = time.time()
print('The total number of words in the book is {}'.format(len(break_into_words())))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))
#END