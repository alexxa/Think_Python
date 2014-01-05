#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 25.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 7. Iteration

# Exercise 7.4

# Write a function called eval_loop that iteratively prompts the user, 
# takes the resulting input and evaluates it using eval, and prints the result.
# It should continue until the user enters 'done', and then return the value of 
# the last expression it evaluated.

def eval_loop():
    result = None
    while True:
        string = str(input('Please enter your expression to evaluate. To finish enter "done".\n'))
        if string != 'done':
            result = eval(string)
            print(result)
        else:
            break
    print('The value of the last expression was {} .You entered "Done"'.format(result))  
    return result
   
  
eval_loop()

#END