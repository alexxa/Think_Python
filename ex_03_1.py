#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 3. Functions

# Exercise 3.1. Move the last line of this program to the top, 
# so the function call appears before the definitions. Run the 
# program and see what error message you get.

#repeat_lyrics() # NameError: name 'repeat_lyrics' is not defined

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()

#END