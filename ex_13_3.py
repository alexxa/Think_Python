#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 13. Case study: data structure selection

#STATUS: check for refactoring

# Exercise 13.3

# Modify the program from the previous exercise to print 
# the 20 most frequently-used words in the book.

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
            
        # I don't know why the following code doesn't work 
        # efficient with big data, however in the book it's said it's
        # 'more concisely' then a variant with if.   
        
        #if word not in dictionary:
        #    print(word)
        #    dictionary[word] = words_list.count(word) # running time is is 22.3023 s
        #    or
        #dictionary[word] = dictionary.get(word, words_list.count(word)) # is smth wrong here?
        
    dictionary.pop('', None)  # accidentally 5 empty strings appeared in the dictionary. why?
    return dictionary

def words_popularity():
    '''
        This function returns the 20 most
         frequently-used words in the book
    '''
    dictionary = create_dict()    
    print(dictionary)
    dict_copy = dictionary
    counter = 0
    popular_words = []
    while counter < 20 :
        popular_word = max(dict_copy, key=dict_copy.get)
        popular_words.append(popular_word)
        dict_copy.pop(popular_word, None)
        counter += 1
    return popular_words
    
    
start_time = time.time()
print('The 20 most frequently-used words in the book: {}'.format(words_popularity()))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))
#END