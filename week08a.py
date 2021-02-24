##
## File: week8a.py (STAT 3250)
## Topic: Vectorized string operations and brief regular expressions
##

#### Vectorized string operations

import pandas as pd # load pandas as pd

# Many of the string operations seen previously can be automatically
# performed across a Series of strings without the use of a for loop.
# Below are some examples.  Let's start with the 'transactions.txt'
# for data.  
lines = pd.Series(open('transactions.txt').read().splitlines())
lines

# We can find the length of each string in 'lines'
lines.str.len()

# We can the start of the word 'Library' in each string
lines.str.find('Library')

# We can count the number of appearances of 'Library' in each string
lines.str.count('Library')

# Or we can just check for 'Library' in each string
lines.str.contains('Library')

# We can mask on the result of 'str.contains' to extract the strings 
# that contain the word 'Library'
newlines = lines[lines.str.contains('Library')]
newlines = pd.Series(newlines)  # Make 'newlines' a Series

# We can pull out the substrings in specific positions from each string
newlines.str[0:24]

# It's also possible to split each string
newlines.str.split()

# Then we can pull out just the time
newlines.str.split().str[3]

# We can split again to get just the seconds
newlines.str.split().str[3].str.split(':').str[2]

# A summary of pandas string operations can be found at
#
#    https://pandas.pydata.org/pandas-docs/stable/text.html
#


#### Regular expressions (very brief intro)

# A future assignment involves translating zip codes into states
# of residence.  In a few cases, the "zip code" is really a
# postal code for a location in Canada.  These can be identified
# by having one or more alphabetic characters ("A-Z") in the
# zip code.  The function 're.search' shown below will 
# determine if a string has any letters in it.

import re # re = "regular expression" which can be used to search

mystr = "00345" # No letter present -- U.S.
if re.search('[a-zA-Z]+', mystr):
    print("Canadian postal code")
else:
    print("U.S. zip code")

mystr = "T5L78" # Letter present -- call it Canada
if re.search('[a-zA-Z]+', mystr):
    print("Canadian postal code")
else:
    print("U.S. zip code")
