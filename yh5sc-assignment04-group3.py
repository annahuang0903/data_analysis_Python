## File: yh5sc-assignment04.py 
## Topic: Assignment 04 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

import pandas as pd;
import numpy as np;

#### Part 1
##
ff = pd.read_csv('fastfood1.csv')

##  (a)
np.mean(ff['secs']) 
#extract the column secs
"""
#1(a)
216.32710792916401
"""

##  (b) 
np.max(ff['secs'])  #max of secs
np.min(ff['secs'])  #min of secs
len(ff[ff['secs']==600])  
#length of dataframe where secs is 600
len(ff[ff['secs']==30])  
#length of dataframe where secs is 30
"""
#1(b)
max: 600
min: 30
#orders with max time: 23
#orders with min time: 123
"""

##  (c) 
np.mean(ff[ff['storenum']==777]['secs'])  
#subset rows of storenum 777 and calculate mean of secs
"""
#1(c)
198.51908396946564
"""

##  (d) 
len(ff[ff['storenum']==321])  
#length of subset of storenum 321
"""
#1(d)
97
"""

##  (e)
np.mean(ff[(ff['storenum']>=700) & (ff['storenum']<=750)]['secs'])
#subset of storenum between 700 and 750, and calculate mean of secs
"""
#1(e)
215.89245446660885
"""

##  (f)
greater=len(ff[(ff['storenum']>=500) & (ff['storenum']<=600) & (ff['secs']>200)])
all=len(ff[(ff['storenum']>=500) & (ff['storenum']<=600)])
#find nomintor and denominator of the proportion
phat=greater/all
lb=phat-1.96*np.sqrt(phat*(1-phat)/all)
ub=phat+1.96*np.sqrt(phat*(1-phat)/all)
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
"""
#1(f)
0.368388686223 0.386205528145
"""

##  (g) 
len(set(ff['storenum']))
#use set to remove duplicates
"""
#1(g)
892
"""

##  (h) 
ff2=ff.groupby('storenum').mean()
#group by storenum and calculate mean of each group
ff3=ff2.sort_values(by='secs')
#sort by mean
ff3.loc[ff3.index[0],:]
#first one is min
ff3.loc[ff3.index[-1],:]
#last one is max
"""
#1(h)
lowest mean order time: 243
highest mean order time: 657
"""

##  (i) 
np.median(ff.groupby('storenum').count())
#group by storenum, count number of orders and calculate median
"""
#1(i)
112.0
"""


#%%

#### Part 2
##
grades = pd.read_csv('samplegrades.csv')

##  (a) 
#np.std(df,ddof=1) gives sample sd
np.mean(grades['CourseAve'])
np.std(grades['CourseAve'],ddof=1)
np.mean(grades['Write'])
np.std(grades['Write'],ddof=1)
"""
#2(a)
mean of Course Average: 80.40115017667841
sample sd of Course Average: 10.666467372530862
mean of Write: 666.7234042553191
sample sd of Write: 94.45561725052345
"""

##  (b)
np.mean(grades[grades['Gender']=='F']['Final'])
#subset female students first
"""
#2(b)
71.35179153094462
"""

##  (c) 
np.mean(grades[(grades['Gender']=='M') & (grades['Sect']=='TR930')]['Final'])
#subsets male students in TR930 first
"""
#2(C)
68.1534090909091
"""

##  (d)
np.mean(grades[grades['Year']==1]['HW'])
np.mean(grades[grades['Year']==4]['HW'])
"""
#2(d)
1st: 189.24376811594195
4th: 192.95172413793105
"""

##  (e) 
l1=len(grades[(grades['Year']==2) & (grades['Sect']=='MW200')])
#number of 2nd year in MW200
l2=len(grades[grades['Year']==2])
#number of 2nd year students
l1/l2
#conditional probability
"""
#2(e)
0.32142857142857145
"""

##  (f) 
grades2=grades.sort_values(by='CourseAve',ascending=False)
#sort by CourseAve in descending order
grades3=grades2.iloc[0:20,:]
#take first 20
np.mean(grades3['CourseAve'])
#calculate mean
"""
#2(f)
95.21865
"""

##  (g) 
grades4=grades[grades['Sect']=='MW200']
#subset students in MW200
grades5=grades4.sort_values(by='Final')
#sort by final in ascending order
grades5.loc[grades5.index[0:10],'Final']
#get the first 10
"""
#2(g)
0.0
27.5
35.0
40.0
45.0
45.0
45.0
45.0
50.0
50.0
"""

##  (h) 
top20CA=grades2.iloc[0:113,:]
#get top 20% of CourseAve
grades6=grades.sort_values(by='APDE',ascending=False)  
#sort by APDE 
top20APDE=grades6.iloc[0:113,:]
#get top 20% of APDE
count=0
for i in range(113):
    for j in range(113):
        if top20CA.iloc[i,:]['StudID']==top20APDE.iloc[j,:]['StudID'] :
            count+=1
#use double for loop to find students in both sets
count/113
"""
#2(h)
0.19469026548672566
"""