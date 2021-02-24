##
## File: week11a.py (STAT 3250)
## Topic: Assignment 9 and More!
##

#### Assignment 9: Dealing with the zip codes

## General Suggestions:
#
# 1) Don't try to blindly merge 'zipcodes.txt' with the other files.
#    It won't work -- at least not well.
#
# 2) Use the zipcodes.txt data to create a new column in 'reviewers.txt'
#    called 'state' that contains for each reviewer (based on the given
#    zip code) one of 'Canada', 'Unknown', or the abbreviation for the
#    reviewers state.
#
# 3) Once 2) is done, *then* merge 'reviewers.txt' with 'reviews.txt'.

                                                     
## More Specific Suggestions:
#
# 1) Create a Series 'zipseries' that has zip codes as the index, and the 
#    corresponding state or territory as the values.

import pandas as pd

zips = pd.read_csv('zipcodes.txt',    # Read in zip codes, eliminate dups
                  usecols = [1,4],
                  converters={'Zipcode':str}).drop_duplicates()
zips

# Create the Series (.values resolves index issues)
zipseries = pd.Series(data=zips['State'].values, index=zips['Zipcode'])
zipseries

# 'zipseries' can be used to look up states and territories, and to 
# decide if a number is actually a zip code.
zipseries['22904']  # Returns the state with zip code '22901'
zipseries['78703']  # Returns the state with zip code '78703'
'22904' in zipseries.index  # Tests if '22904' is a zip code
'00000' in zipseries.index  # Tests if '00000' is a zip code

# 2) Define a function that takes a string as input and returns one
#    of 'Canada', 'Unknown', or a state/territory code.
#
# Basic framework:
#
# def ziptostate(zcode):
#       if zcode includes a letter:
#           return('Canada')
#       elif zcode is in the zipseries index:
#           return(zipseries[zcode])
#       else:
#           return('Unknown')

# 3) Use '.apply' to run each reviewer's zip code through 'ziptostate'
#    then use the resulting Series as a new column for 'reviewers.txt'

# 4) Once 3) is done, then merge 'reviewers.txt' with the other data.
    
    
#### Concatenating Data Frames

# Define df1 and df2
df1 = pd.DataFrame({'J': [3,5,6,7],
                    'K': [8,3,2,5],
                    'L': [6,8,6,3]})
df1
df2 = pd.DataFrame({'J': [3,4,6,7,8],
                    'K': [4,7,0,11,3],
                    'L': [5,5,6,2,8]})
df2

# Concatenate df1 and df2 by rows
newdf = pd.concat([df1,df2])
newdf

#### Searching directories

import glob # 'glob' searches for files

# Reminder: Change to directory 'Week11'

# '*.csv' selects files ending in '.csv'
filelist = glob.glob('*.csv') # 'glob.glob' -- hee hee
filelist

# The above list allows us to iterate through the files to read
# them in, one at a time.
for f in filelist:
    df = pd.read_csv(f)
    print(df,"\n")

# We can concatenate the dataframes into one large dataframe

df = pd.DataFrame()
for f in filelist:
    newdf = pd.read_csv(f)
    df = pd.concat([df,newdf])
df







