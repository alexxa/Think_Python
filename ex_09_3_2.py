#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 27.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.3.2
# Modify your program to prompt the user to enter a string of 
# forbidden letters and then print the number of words that 
# dont contain any of them.


def avoids(word, string):
    for letter in word:
        if letter in string:
            return False
    return True

string = str(input('Please enter the string of forbidden letters:\n'))

fin= open('words.txt')
count = 0
for word in fin:
    word = word.strip()
    if avoids(word, string):
        count += 1
        print (word)
print('The total number of words that donot contain any letter from "{}" is {}'.format(string, count))
# dont contain any of them')   
#print(avoids('banana', 'ktmu'))
#print(avoids('banana', 'ktma'))
#END