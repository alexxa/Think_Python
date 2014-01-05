#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.4

# Modify find so that it has a third parameter, the index 
# in word where it should start looking.

# My solution is not case sensitive and checks whether 
# there is more then once occurrence of the given letter.

def find(word, letter, index):
    word, letter = word.lower(), letter.lower()
    print('We look for a letter "{}" in the word "{}"'.format(letter, word))
    while index < len(word):
        if word[index] == letter:
            print(index) 
        index = index + 1
    return -1

find('Mama', 'm', 0)
print()
find('Mamaaaaaaaa', 'a', 5)

#END