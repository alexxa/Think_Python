#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 29.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 13. Case study: data structure selection

# Exercise 13.5

# Write a function named choose_from_hist that takes a histogram
# as defined in Section 11.1 and returns a random value from the
# histogram, chosen with probability in proportion to frequency.
# For example, for this histogram:

# >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> print hist
# {'a': 2, 'b': 1}

# your function should return 'a' with probability 2/3 and 'b' 
# with probability 1/3.

import random, time

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def sum_dict_values(*t):
    return sum(t)

def choose_from_hist(h):
    print(h)
    random_key = random.choice(list(h.keys()))
    probability = h[random_key]/sum(h.values())
    values_sum = sum(h.values())
    print('Random value is "{}" and its probability is {}/{}, i.e. {}.' \
          .format(random_key, h[random_key], sum(h.values()), probability))
    
start_time = time.time()
#h=histogram('brontosaurus')
h=histogram('aba')
choose_from_hist(h)
function_time = time.time() - start_time

print('\nRunning time is {0:.4f} s'.format(function_time))

#END