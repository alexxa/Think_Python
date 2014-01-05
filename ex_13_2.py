#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 13. Case study: data structure selection

# Exercise 13.2

# Go to Project Gutenberg (http://gutenberg.org) and download
# your favorite out-of-copyright book in plain text format.

# Modify your program from the previous exercise to read the 
# book you downloaded, skip over the header information at the 
# beginning of the file, and process the rest of the words as 
# before.

# Then modify the program to count the total number of words
# in the book, and the number of times each word is used.

# Print the number of different words used in the book. Compare 
# different books by different authors, written in different
# eras. Which author uses the most extensive vocabulary?
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
        This function reads file, breaks it into 
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
        This function calculates words frequency and
        returns it as a dictionary.
    '''
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
       
    return dictionary

dictionary = create_dict()
dictionary.pop('', None)  # accidentally 5 empty strings appeared in the dictionary. why?
    

#print('The total number of words in the book is {}'.format(len(break_into_words())))
#print('The number of different words used in the book {}'.format(len(dictionary)))

start_time = time.time()
print('The total number of words in the book is {}'.format(len(break_into_words())))
print('The number of different words used in the book {}'.format(len(dictionary)))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))
#END