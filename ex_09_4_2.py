#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 27.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play
# Exercise 9.4

# Can you make a sentence using only the letters acefhlo? 
# Other than Hoe alfalfa?

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True

string = 'acefhlo'
fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if word != 'hoe' and word != 'alfalfa':
        if uses_only(word, string):
            count +=1
            print(word)
print('You have {} words which contain only "acefhlo" letters to make a sentance.'.format(count))
# This code returns

#END