#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 27.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.6

# Write a function called is_abecedarian that returns True 
# if the letters in a word appear in alphabetical order 
# (double letters are ok). How many abecedarian words are 
# there?

def is_abecedarian(word):
    index = 0
    while index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True
    
fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
print('There are {} abecedarian words.'.format(count))   
#print(is_abecedarian('banana'))
#print(is_abecedarian('abcdefg'))
#END