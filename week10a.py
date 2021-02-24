##
## File: week10a.py (STAT 3250)
## Topic: TBD
##

#### Zip codes

import pandas as pd

## Reading the zip code file

# The optional argument 'usecols' allows you to specify specific
# columns for importing, and ignore the rest
zips = pd.read_csv('zipcodes.txt', usecols = [1,4])
zips

# Zip codes sometimes have leading zeros -- for instance, the
# zip code for Amherst, MA is 01002.  Pandas sees the zip codes
# as numbers, and drops the leading zeros.  We want to load the
# zip codes as strings, since that will match the format in the
# file 'reviewers.txt' file.
zips = pd.read_csv('zipcodes.txt',
                  usecols = [1,4],
                  converters={'Zipcode':str})
zips

## Merging data sets

# Let's start with two simple data frames, to use as an illustration.
df1 = pd.DataFrame({'student':['Jim','Jane','Bob','Ann'],
                    'major':['English','Math','Math','CompSci']})
df1

df2 = pd.DataFrame({'student':['Ann','Bob','Jim','Jane'],
                    'year':[2,3,4,3]})
df2

# Both data frames have a column 'student' with the same students
# names in each.  The function 'pd.merge' recognizes the common
# column, and creates a new data frame that combines df1 and df2.
df3 = pd.merge(df1,df2)
df3

# Now suppose we have another data frame 'df4' that includes the
# name of majors and the building.
df4 = pd.DataFrame({'building':['Bryan','Kerchof','Rice'],
                    'major':['English','Math','CompSci']})
df4

# If we apply 'pd.merge' to df3 and df4, the two data frames
# are merged together based on the common column 'major'.
df5 = pd.merge(df3,df4)
df5

# Let's add one more data frame, this one with the student's
# favorite classes.
df6 = pd.DataFrame({'student':['Ann','Bob','Bob','Jim','Jane','Jane','Jane'],
                    'fav':['STAT 3250','MATH 4140','MATH 3350','SOC 2001',
                           'MATH 4140','MATH 3100','MATH 3310']})
df6

# Here's what we get if we merge df5 and df6:
df7 = pd.merge(df5,df6)
df7

# Aside: You can specify the merge key, if the default is not what
# you want.  (Or you just want it to be explicit.)
df7 = pd.merge(df5,df6, on='student')
df7

df8 = pd.DataFrame({'school':['College','College','College','College','SEAS'],
                    'major':['English','Math','Math','CompSci','CompSci']})
df8

# There is a duplicate row in df8.  We can remove this using 
# 'drop_duplicates()'
df8 = df8.drop_duplicates() 
df8

# Here's what we get when we merge df7 and df8:
df9 = pd.merge(df7,df8, on='major')
df9

# This new data frame might not be what we want -- Anne's school
# of enrollment is not clear.  The moral: Be careful with merging, and
# make sure it's doing what you want!








