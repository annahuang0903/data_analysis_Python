##
## File: week9a.py (STAT 3250)
## Topic: Dates and Times
##

#### Dates and Times -- Part 1

import datetime
import pandas as pd

t = datetime.time(1, 2, 3, 4) # '.time' is just times
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)


today = datetime.date.today() # Gives today's date, not time
print(today)
type(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)

rightnow = datetime.datetime.now() # Date and time
rightnow  # No format
print(rightnow) # Generic format
format = "%a %b %d %H:%M:%S %Y"
print(rightnow.strftime(format))

format = "%A %B %d %Y %H:%M:%S"
print(rightnow.strftime(format))

format = "%A %m-%d-%y %H:%M:%S"
print(rightnow.strftime(format))

# 'fromtimestamp' gives date/time in local time
datetime.datetime.fromtimestamp(1347517491)
datetime.datetime.fromtimestamp(0) # Start time, local time
datetime.datetime.utcfromtimestamp(0) # Start time, UTC

# We can also set the format.
datetime.datetime.fromtimestamp(1347517491).strftime(format)
