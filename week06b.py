##
## File: week6b.py (STAT 3250)
## Topic: A bit more "GroupBy" and some "Apply"
##

## NOTE: There is no "week6a.py" because Monday was 
##       Fall Break.

import pandas as pd # load pandas

## Start with GroupBy
                
# We need a new practice DataFrame
df = pd.DataFrame({'C2':['x','y','x','x','x','y','x','y'],
                   'C3':[1,3,-2,-4,5,7,0,2],
                   'C4':[8,0,5,-3,4,1,3,1],
                   'C5':[3,-1,0,-2,4,3,8,0]},
                    index = ['a','a','b','b','c','c','a','c'])
df

# Previously we saw how to group by a column (or several
# columns) in a data frame, but we can also GroupBy the
# index.
group1 = df['C3'].groupby(df.index) # Group by the index
group1.sum() 

# Two other features
list(group1)  # Lists the groups, although not nicely formatted
group1.describe()  # A nice table of summary information


## Apply and MapApply

# Let's start with a sample function

def mysgn(x): # Returns the "sign" of x
    if x > 0:
        return(1) # 1 when x positive
    elif x < 0:
        return(-1) # -1 when x negative
    else:
        return(0) # 0 when x is 0

mysgn(-3) # Test values
mysgn(0) 
mysgn(2) 
 
# Next we need a sample Series
s1 = pd.Series([2,-5,0,2,-6,-4])
s1

# "apply" works on a Series, and will apply the called
# function to each element of the series

s1.apply(mysgn) # Applies "mysgn" to each element of s1

# apply will work on a single column of a DataFrame, which
# is really a Series in disguise
df['C4'].apply(mysgn)

# apply won't work on more than one column
df[['C4','C3']].apply(mysgn)

# But a variant "applymap" will work on multiple columns
# of a DataFrame
df[['C4','C3']].applymap(mysgn)


## Apply and GroupBy together!

# There are only a handful of functions that will work
# automatically with GroupBy, but we can define our own.    

# A sample function.  It must take a DataFrame as input,
# and return a DataFrame, Series, or scalar as output.
# Note that the function will probably need to be tailored
# to the specific DataFrame being grouped.

# This function will determine the range (max - min) of
# values in the column 'C3'
def myrange(x):
    ran = x['C3'].max() - x['C3'].min()
    return(ran)

# Applying "myrange" to our DataFrame df:
myrange(df)
df          # Check the output

# We would like to apply this function to the grouped
# version of df, so that we get the range for each group

# First we group.  Note that we don't group just df['C3']
# because that doesn't work because df['C3'] is a Series
group2 = df.groupby(df.index)

# Now we append "apply(myrange)" in order to get the range
# for each group.
group2.apply(myrange)
df   # One more check

