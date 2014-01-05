#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 3. Functions

# Exercise 3.2. Move the function call back to the bottom and 
# move the definition of print_lyrics after the definition of 
# repeat_lyrics. What happens when you run this program?.


# no error!
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    
repeat_lyrics()


#END