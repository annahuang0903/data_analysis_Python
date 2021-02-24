##
## File: week10b.py (STAT 3250)
## Topic: DataFrame column operations
##

#### DataFrame examples

import pandas as pd

c1 = ['A','B','C','D','A','B','C','B','C','D','A','B','B']
c2 = ['X','Y','Y','X','Y','Y','X','X','X','Y','Y','X','Y']
c3 = [ 1,  1,  0,  0,  1,  0,  0,  1,  1,  1,  0,  1,  0 ]
c4 = [ 0,  1,  1,  1,  0,  0,  1,  0,  1,  0,  0,  1,  1 ]
c5 = [ 0,  0,  1,  0,  0,  1,  1,  0,  1,  0,  1,  0,  1 ]
c6 = [ 5,  1,  7,  3,  3,  2,  6,  4,  3,  1,  7,  3,  5 ]
df = pd.DataFrame({'Col1':c1, 
                   'Col2':c2, 
                   'Col3':c3, 
                   'Col4':c4, 
                   'Col5':c5,
                   'Col6':c6})
df

## Find the proportions of Col2 for each type in Col1.

# Start with the counts for all combinations of Col1 and Col2
groupn = df['Col1'].groupby([df['Col1'],df['Col2']])
num = groupn.count()
num

# Next we find the counts for just Col1
groupd = df['Col1'].groupby(df['Col1'])
den = groupd.count()
den

# If we divide 'num' by 'den', then we get the proportions for
# each type in Col1
props = num/den
props

# If we just want the entries where Col2 = 'Y':
props[:,'Y']

# These can be sorted, with the largest and smallest extracted
props[:,'Y'].sort_values()[[0,-1]]

## Column operations

# We can slice columns from a DataFrame using '.loc':
nums = df.loc[:,'Col3':'Col6']
nums

# Recall that we can add the columns or rows with 'sum'
nums.sum(axis=0)  # The column sums
nums.sum(axis=1)  # The row sums

# We can multiply one column times another.
nums['Col4']*nums['Col6']

# Several multiplications can be done at the same time by
# using '.multiply' as shown.
prods = nums.loc[:,'Col3':'Col5'].multiply(nums['Col6'], axis='index')
prods

# These new columns can be added:
tots = prods.sum(axis=0)
tots

# We can also add the old columns, which gives a count of nonzero terms.
cts = nums.loc[:,'Col3':'Col5'].sum(axis=0)
cts

# We can divide 'tots' by 'cts' to get an average of the nonzero terms.
tots/cts
