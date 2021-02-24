##
## File: week5b.py (STAT 3250)
## Topic: "GroupBy" in pandas; Modifying a dataframe
##

## NOTE: There is no "week5a.py" because Monday was only in-class
##       work on assignments, with no presentation.

import pandas as pd # load pandas
                
# We need a new practice DataFrame
df = pd.DataFrame({'C1':['a','a','b','b','c','c','a','c'],
                   'C2':['x','y','x','x','x','y','x','y'],
                   'C3':[1,3,-2,-4,5,7,0,2],
                   'C4':[8,0,5,-3,4,1,3,1],
                   'C5':[3,-1,0,-2,4,3,8,0]})
df

# The GroupBy function allows us to group rows
# of a DataFrame based on the values in one of
# the columns, and then perform operations
# based on those groupings.  Examples follow.

# Here we group the data in column 'C3' based on the
# entries in column 'C1'
group1 = df['C3'].groupby(df['C1']) 
group1 # No computations yet, just a GroupBy object

group1.mean() # Mean for each of group a, b, c
group1.std(ddof=1) # SD for each of group a, b, c
group1.count() # The number of elements in each group
group1.max() # The maximum value from each group
group1.min() # The minimum value from each group
group1.sum() # The sum of the values in each group

# The above computations return a Series, so you can
# apply the usual Series operations on it.
group1.mean().iloc[0:2] # The first two rows
group1.sum().loc['c'] # The entry indexed by 'c'
group1.max().loc['a':'b'] # Entry 'a' to 'b'
group1.median().sort_values()  # Sort on the values

# Group can be extracted by key using 'get_group'
group1.get_group('a')

# We can have more than one data column
group2 = df[['C3','C4']].groupby(df['C2'])
group2.mean()

# All the columns can be grouped
group3 = df.groupby(df['C2'])
group3.mean() # Strings don't have means, so 'C1' ignored
group3.count() # Strings do have counts, so 'C1' included

# GroupBy can be used to group on more than one key.
# Here we group on the keys in C1 and C2.
group4 = df['C5'].groupby([df['C1'],df['C2']])
df # Reminder of original DataFrame
group4.mean() # Mean for each group
group4.mean()['c','x'] # Mean for group ('c','x')
group4.mean().iloc[4] # The 5th entry in Series

#%%

## Adding and removing columns to a dataframe, changing values

# Reset the dataframe
df = pd.DataFrame({'C1':['a','a','b','b','c','c','a','c'],
                   'C2':['x','y','x','x','x','y','x','y'],
                   'C3':[1,3,-2,-4,5,7,0,2],
                   'C4':[8,0,5,-3,4,1,3,1],
                   'C5':[3,-1,0,-2,4,3,8,0]})
df

# We can create an empty DataFrame column 
df['C6'] = ""
df

# Or we can add values to the column
df['C6'] = 13
df

# We can perform arithmetic on columns to create new columns
df['C7'] = df['C4']+df['C5']
df

# Or modify old columns
df['C6'] = df['C5'] - 2*df['C4']
df

# We can change individual entries with '.loc':
df.loc[3,'C6'] = 100  # Here '3' is in both the explicit and impicit index
df

# We can add lots of entries with a loop.
for i in range(len(df)):
    df.loc[i,'C8'] = i**2 # If column does not exist it is created.
df['C8'] = "a"
df

# Use '.loc'!! -- leaving it off does not work as expected!!
df[3,'C6'] = 100  # Don't do this!

# Let's remove the unwanted column
df.columns  # Here's the column list
df = df.drop((3,'C6'), axis=1) # 'axis=1' specifies columns; 'axis=0' is rows
df

# Just for fun, let's remove a row too
df = df.drop(5, axis=0)  # Removing a row from the middle is fine
df

# We'll discuss adding rows at another time.

#%%