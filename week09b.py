##
## File: week9b.py (STAT 3250)
## Topic: Dates and Times
##

#### Dates and Times -- Part 2

import datetime
import pandas as pd

## A quick review

# Convert a single timestamp to a 'datetime' object
dt = datetime.datetime.utcfromtimestamp(881250949)
dt
type(dt)
print(dt)  # 'print' has a default format for printing datetime objects

## The pandas version

# pandas provides a function that works the same way.  The argument
# 'unit' specifies the time units -- here it is seconds.  The default
# is UTC.
ts = pd.to_datetime(881250949, unit='s')
print(ts)

# We can get a different format using 'strftime'
format = "%a %b %d %H:%M:%S %Y"
print(ts.strftime(format))

# Or just put the format in strftime
print(ts.strftime("%B %d %Y"))
print(ts.strftime("%B %-d %Y"))  # Day without the zero padding

# We can extract parts of the datetime object by specifying
# the part directly or through 'strftime'
ts
ts.month
ts.hour
ts.strftime('%Y')
ts.strftime('%b')

# A table of 'strftime' format codes is available at http://strftime.org/

## Series of timestamps

# Suppose that we have a Series of timestamps to process.

timestamps = pd.Series([881250949,891717742,878887116,880606923,886397596])
timestamps

# We can try 'datetime.datetime' ....
datetime.datetime.utcfromtimestamp(timestamps)  # Nope

# The pandas 'to_datetime' will take a Series as input and produce a Series
# of numpy datetime objects as output.
dts = pd.to_datetime(timestamps, unit='s')
dts
print(dts)

# As above, it is possible to extract portions of the objects, but now it
# is vectorized!  For a Series we have to add 'dt' as shown. (This is similar  
# to 'str' for vectorizing string operations.)
dts.dt.year
dts.dt.hour
dts.dt.month
dts.dt.dayofweek
dts.dt.strftime('%A')
dts.dt.strftime('%A %b %-d')




