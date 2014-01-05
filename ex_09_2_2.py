#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 26.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 9. Case study: word play

# Exercise 9.2.1

# Modify your program ex_9_1 from the previous section to 
# print only the words that have no e and compute
# the percentage of the words in the list have no e.

def has_no_e(word):
    word = word.lower()
    for letter in word:
        if letter == 'e':
            return False
    return True


fin = open('words.txt')
total_words = 0
no_e_words = 0

for word in fin:
    word = word.strip()
    total_words +=1
    if has_no_e(word):
        no_e_words +=1
        print(word)
#print(total_words, no_e_words)
print('The percentage of the words in the list have no e: {0:.2f}%'.format(no_e_words/total_words*100))

#END