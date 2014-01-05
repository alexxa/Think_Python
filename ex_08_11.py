#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 8. Strings

# Exercise 8.11
# The following functions are all intended to check whether 
# a string contains any lowercase letters, but at least some 
# of them are wrong. For each function, describe what the 
# function actually does (assuming that the parameter is a string).

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# any_lowercase1(s) is wrong since it tests for lowercase/uppercase
# only the first letter of the string.and returns True/False respectively



def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# any_lowercase2(s) is wrong since it returns True. It checks whether
# 'c' is lowercase and this function doesn't check any letter from the given string 

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag
    
# any_lowercase3(s) is wrong since it returns True/False depending only on the last
# letter of the string. 
 
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag
# any_lowercase4 is fine!

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# any_lowercase5(s) is wrong since it checks whether ALL letters in a string are lowercase

print(any_lowercase1('Banana'))
print(any_lowercase2('BANANA'))
print(any_lowercase3('bananA'))
print(any_lowercase4('bANANA'))
print(any_lowercase5('bananA'))

#END