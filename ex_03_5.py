#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 24.12.2013
#SOURCE: Think Python: How to Think Like a Computer Scientist by Allen B. Downey
# http://www.greenteapress.com/thinkpython/html/index.html
#PURPOSE: Chapter 3. Functions

# Exercise 3.5

# This exercise can be done using only the statements and other 
# features we have learned so far.
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# 2. Write a function that draws a similar grid with four rows and 
# four columns.

# My solution works for any number of rows and columns

def print_straight_slash_line(lines):
    print(lines)
    print(lines)
    print(lines)
    print(lines)

def grid_plus_line(num_of_columns):    
    columns = (' + - - - -')*num_of_columns + ' +'
    print(columns)
    
def grid_row(num_of_columns):
    grid_plus_line(num_of_columns)
    
    lines = (' |        ')*num_of_columns + ' |'
    print_straight_slash_line(lines)
    
def grid_rows(num_of_rows, num_of_columns):
    while num_of_rows > 1:
        grid_row(num_of_columns) 
        num_of_rows -=1
      
def grid(num_of_rows, num_of_columns):
    grid_row(num_of_columns)
    grid_rows(num_of_rows, num_of_columns)
    grid_plus_line(num_of_columns)
    
    
grid(1,1)
print()
grid(2,2)
print()
grid(8,8)
print()
grid(1,8)
print()
grid(8,1)
#END