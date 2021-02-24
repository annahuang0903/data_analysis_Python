##
## File: week7b.py (STAT 3250)
## Topic: More string operations
##

#### A demonstration of string searching

# We start by reading in the file 'transactions.txt'
alllines = open('transactions.txt').read().splitlines()

import numpy as np # load numpy as np
import pandas as pd # load pandas as pd

## Question 1: 
#   What schools have problems referenced in the file?
#   How many times is each school referenced?
#   (These are listed second in the 'Library/...' string.)

## Sample solution

# Let's start by pulling out the lines that have the required string
# in them.
newlines = []  # A new list for the required lines from 'alllines'
for line in alllines:
    if line.count("Library") > 0:
        newlines.append(line)    #Append the lines containing 'Library'
print(newlines)  # Seems correct

# Next we grab the first line from 'newlines' to use for practice.
temp = newlines[0]
print(temp)

# Since the school name appears between the 1st and 2nd occurance of '/'
# we can split on '/' and pull out the second entry.  Let's try it on
# the temp string.
temp.split('/') # Just the split, to see what happens
temp.split('/')[1] # The second entry

# Looks like it works, so let's go through the entire list.
schools = []  # Empty list to hold schools
for line in newlines:
    schools.append(line.split('/')[1]) # Append school name to list
print(schools)  # Check the results

np.unique(schools)  # This gives the unique schools
pd.Series(schools).value_counts()  # Convert to Series to use 'value_counts'

## Question 2
#   Obtain a list of the different unique problem file names.  These are the 
#   names that end in '.pg'.

## Sample solution

# The '.pg' names come at the end of the substring that starts with 'Library'.
# Here's our practice line again: 
print(temp)

# Let's split on ' ' (spaces):
temp.split(' ')

# It turns out that some of the spaces are actually tabs, indicated by '\t'
# Let's try splitting on those instead.
temp.split('\t')

# This is more promising.  The substring with the '.pg' in it is 4th in the
# split list:
temp.split('\t')[3]

# The substring can be split again, this time on '/':
temp.split('\t')[3].split('/')

# We want the list item in this new list:
temp.split('\t')[3].split('/')[-1]

# Now that this seems to be working, let's run through the full set of lists,
# extract out the problem names, and put them in a new list.
problems = []  # Empty list to hold problem names
for line in newlines:
    problems.append(line.split('\t')[3].split('/')[-1]) # Append to prob. list
print(problems)  # Check the results

np.unique(problems)  # The unique problem names
np.unique(problems).tolist()  # Same thing, but as list and without ...
  
    
#### Specialized function

# Assignment 6 has a question that may require determining if a given 
# character is a digit.  The demo below can be used for this.

str.isdigit("23")  # Yes!
str.isdigit("STAT3250")  # No!

