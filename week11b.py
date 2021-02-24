##
## File: week11b.py (STAT 3250)
## Topic: Dates
##

#### Dates -- Part 2b

import pandas as pd

# We're focusing here on the dates in the stock price files.

stocks = pd.read_csv('AA.csv') # File of stock prices
stocks

# Here's the data types.
stocks.dtypes # Default data types for the columns
stocks.loc[0,'Date'] - stocks.loc[1,'Date'] # Not a date!

# Here's one way to convert the column so that Pandas recognizes
# the entries as dates.
stocks['Date'] = pd.to_datetime(stocks['Date']) # Convert to dates
stocks.dtypes

# We can identify the month, year, and day of the week:
stocks['Date'].dt.month
stocks['Date'].dt.year
stocks['Date'].dt.dayofweek

# It's possible to use inequalities on dates
stocks['Date'] < '2014-12-10'
(stocks['Date'] < '2014-12-19') & (stocks['Date'] > '2014-12-08')

# The above combines well with masking
stocks[stocks['Date'].dt.year == 2012]
stocks[(stocks['Date'] < '2014-12-19') & (stocks['Date'] > '2014-12-08')]
stocks.loc[stocks['Date'].dt.dayofweek == 0, 'Open']

# And we can do arithmetic
a = stocks.loc[0,'Date'] - stocks.loc[7,'Date']
a
b = stocks.loc[0,'Date'] - stocks.loc[5,'Date']
b

a/b # This comes up when interpolating








