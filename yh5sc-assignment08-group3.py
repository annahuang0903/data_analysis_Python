## File: yh5sc-assignment08.py 
## Topic: Assignment 08 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

## 1. 
import pandas as pd # load pandas as pd
reviews = pd.read_csv('reviews.txt', 
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date'])

##  (a) 
#find minimum seconds as oldest time
oldest=pd.to_datetime(reviews['Date'].min(),unit='s')
#find maximum seconds as most recent time
recent=pd.to_datetime(reviews['Date'].max(),unit='s')
#print in correct format
print(oldest.strftime("%Y-%m-%d %H:%M:%S"))
print(recent.strftime("%Y-%m-%d %H:%M:%S"))
"""
1(a)
oldest: 1997-09-20 03:05:10
most recent: 1998-04-22 23:10:38
"""

##  (b) 
#calculate median time
median=pd.to_datetime(reviews['Date'].median(),unit='s')
#print in correct format
print(median.strftime("%A %B %d %Y %H:%M:%S"))
"""
1(b)
Monday December 22 1997 21:42:24
"""

##  (c) 
reviews['month']=pd.to_datetime(reviews['Date'],unit='s').dt.month
#group by month and calculate average rating
reviews['Rating'].groupby(reviews['month']).mean()
"""
1(c)
month
1     3.397730
2     3.455009
3     3.548831
4     3.574848
9     3.540125
10    3.591421
11    3.559842
12    3.580388
"""

##  (d) 
reviews['day']=pd.to_datetime(reviews['Date'],unit='s').dt.weekday_name
#group by day and count rating and sort values
reviews['Rating'].groupby(reviews['day']).count().sort_values(ascending=False)
#max number is last line 
"""
1(d)
Wednesday    16621
"""

##  (e) 
#group by reviewe and count number of ratings and sort values
reviews['Rating'].groupby(reviews['Reviewer']).count().sort_values(ascending=False)
#top 5 are 405, 655, 13, 450,276
top5=[405, 655, 13, 450,276]
#create new list
times=[]
#find first review time of each reviewer and append to list
for i in top5:
    df=reviews[reviews['Reviewer'] == i]
    time=pd.to_datetime(df['Date'].min(),unit='s').strftime("%Y-%m-%d %H:%M:%S")
    times.append(time)
times
"""
1(e)
['1998-01-23 08:37:15',
 '1998-02-14 02:52:00',
 '1997-12-07 17:11:23',
 '1997-12-15 19:53:37',
 '1997-09-20 20:12:17']
"""

## 2.
##  (a) 
#read in file
lines = pd.Series(open('pizza_requests.txt').read().splitlines())
#subset unix_timestamp_of_request_utc
request=lines[lines.str.contains("unix_timestamp_of_request_utc")]
#split line
times=[]
for i in request:
    times.append(pd.to_numeric(i.split(", ")[1]))
#find minimum seconds as oldest time
oldest=pd.to_datetime(pd.Series(times).min(),unit='s')
#find maximum seconds as most recent time
recent=pd.to_datetime(pd.Series(times).max(),unit='s')
#print in correct format
print(oldest.strftime("%Y-%m-%d %H:%M:%S"))
print(recent.strftime("%Y-%m-%d %H:%M:%S"))
"""
2(a)
oldest: 2011-02-14 22:28:57
most recent: 2013-10-12 01:30:36
"""

##  (b) 
#calculate median time
median=pd.to_datetime(pd.Series(times).median(),unit='s')
#print in correct format
print(median.strftime("%A %B %d %Y %H:%M:%S"))
"""
2(b)
Friday July 20 2012 17:54:08
"""

##  (c) 
#create new list and extract hour
hours=pd.to_datetime(pd.Series(times),unit='s').dt.hour
#count number of requests in each hour and sort
pd.Series(hours).value_counts().sort_values(ascending=False).iloc[0:5]
"""
2(c)
0     508
22    497
23    491
21    464
1     441
"""

##  (d)
#subset requester_received_pizza
receive=lines[lines.str.contains("requester_received_pizza")]
#create new list
status=[]
#extract received pizza status and append to list
for i in receive:
    status.append(i.split(", ")[1])
#combine hours and status columns
pizza=pd.concat([pd.Series(hours), pd.Series(status)], axis=1)
#subset true received 
success=pizza[pizza[1]=="true "]
#count true value of each hour
count=(success[1].groupby(success[0]).count()).to_frame()
#get total number of each hour
total=(pizza[1].groupby(pizza[0]).count())
#create new columns to store proportion of each type
count['proportion']=""
for i in range(len(count)):
    count['proportion'].iloc[i]=count[1].iloc[i]/total.iloc[i]
#show proportions
count['proportion'].sort_values(ascending=False)
#highest proportion is first line
"""
2(d)
13     0.349398
"""

##  (e) 
#following from (d), lowest proportion is last line
"""
2(e)
8     0.0810811
"""




