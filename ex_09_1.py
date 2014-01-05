#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 26.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.1
# Write a program that reads words.txt and prints only the words
# with more than 20 characters (not counting whitespace).


fin = open('words.txt')
for word in fin:
    word = word.strip()
    if len(word) > 20:
        print(word)


#END