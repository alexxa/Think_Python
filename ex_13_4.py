#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 13. Case study: data structure selection

#STATUS: check for refactoring, complete see *

# Exercise 13.4

# Modify the previous program to read a word list (see Section 9.1)
# and then print all the words in the book that are not in the word
# list. 


# * How many of them are typos? How many of them are common 
# words that should be in the word list, and how many of them are 
# really obscure?  - Mmm ?

import string, time

def del_punctuation(item):
    '''
        This function deletes punctuation from a word.
    '''
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item 

def break_into_words():
    '''
        This function reads file (book), breaks it into 
        a list of used words in lower case.
    '''
    book = open('tsawyer.txt')
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            #print(item)
            words_list.append(item)
    return words_list

def create_dict():
    '''
        This function calculates words frequency (in a book) and
        returns it as a dictionary.
    '''
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
        
    dictionary.pop('', None)  # accidentally 5 empty strings appeared in the dictionary. why?
    return dictionary

def words_list():
    '''
        This function returns words list from words.txt file.
    '''
    res = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

def avoids():
    dictionary = words_list()
    book = create_dict()
    count = 0
    for i in book:
        if i not in dictionary:
            print(i)
            count += 1
    print()
    print('In total there are {} words which are not in words.txt file'.format(count))

   
start_time = time.time()
avoids()
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))

# I see there are many typo like promisedhe, thoughnothings,
# sakethats or jamthats, etc.. I don't think it's because of the code, 
# but text 'quality'.
#END
