## File: yh5sc-assignment05.py 
## Topic: Assignment 05 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

#### Part 1
import pandas as pd;
import numpy as np;
##

ff = pd.read_csv('fastfood2.csv')

##  (a) 
len(ff[ff['meal']=="Lunch"])/len(ff['meal'])
"""
1(a)
0.5165224154435226
"""

##  (b) 
ff['secs'].groupby(ff['dayofweek']).mean()
"""
1(b)
dayofweek
Fri     216.234941
Mon     216.774747
Thur    216.605129
Tues    215.742300
Wed     216.282449
"""

##  (c) 
#breakfast
#calculate proportion
phat=len(ff[(ff['meal']=="Breakfast")&(ff['drinkonly']=="Yes")])/len(ff[ff['meal']=="Breakfast"])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(ff[ff['meal']=="Breakfast"]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(ff[ff['meal']=="Breakfast"]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.221174066568 0.236133943342
#lunch
#calculate proportion
phat=len(ff[(ff['meal']=="Lunch")&(ff['drinkonly']=="Yes")])/len(ff[ff['meal']=="Lunch"])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(ff[ff['meal']=="Lunch"]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(ff[ff['meal']=="Lunch"]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.126757194582 0.132542818931
#dinner
#calculate proportion
phat=len(ff[(ff['meal']=="Dinner")&(ff['drinkonly']=="Yes")])/len(ff[ff['meal']=="Dinner"])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(ff[ff['meal']=="Dinner"]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(ff[ff['meal']=="Dinner"]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.127304761188 0.134234123272
"""
1(c)
Breakfast: (0.221174066568 0.236133943342)
Lunch: (0.126757194582 0.132542818931)
Dinner: (0.127304761188 0.134234123272)
Breakfast is different from lunch and dinner with a higher proportion of
drinkonly, but lunch and dinner are similar.
"""

##  (d)
#group by meal, calculate mean of cost
ff['cost'].groupby(ff['meal']).mean()
"""
1(d)
meal
Breakfast    292.079191
Dinner       502.017676
Lunch        372.363622
"""

##  (e) 
#get count of each type for each day, convert to data frame
day=(ff['meal'].groupby([ff['dayofweek'],ff['meal']]).count()).to_frame()
#get total number of meals each day and repeat 3 times for each day
total=(ff['meal'].groupby(ff['dayofweek']).count()).repeat(3).to_frame()
#create new columns to store proportion of each type
day['proportion']=""
for i in range(len(day)):
    day['proportion'].iloc[i]=day['meal'].iloc[i]/total['meal'].iloc[i]
day['proportion']
"""
1(e)
dayofweek  meal     
Fri        Breakfast    0.121418
           Dinner       0.358544
           Lunch        0.520038
Mon        Breakfast    0.120165
           Dinner       0.364263
           Lunch        0.515572
Thur       Breakfast    0.122454
           Dinner       0.361479
           Lunch        0.516067
Tues       Breakfast    0.119838
           Dinner       0.363722
           Lunch        0.516441
Wed        Breakfast    0.119902
           Dinner       0.365632
           Lunch        0.514467
"""

##  (f) 
avg=ff['secs'].groupby(ff['storenum']).mean().to_frame()
#calculate mean average
mean_avg=ff['secs'].groupby(ff['storenum']).mean().mean()
#calculate standard deviation of mean
sd=ff['secs'].groupby(ff['storenum']).mean().std(ddof=1)
#calculate bound
ubound=mean_avg+sd*2
lbound=mean_avg-sd*2
#high performance
high_mean=avg[avg['secs']<lbound].index
high_mean
#low performance
low_mean=avg[avg['secs']>ubound].index
low_mean
"""
1(f)
high performance: [ 27,  43,  53, 122, 201, 243, 312, 500, 511, 514, 550, 570, 651,
            699, 722, 852, 859],
low performance: [ 30,  47,  59, 128, 149, 154, 155, 231, 233, 281, 318, 387, 392,
            402, 422, 452, 474, 528, 614, 621, 657, 718, 723, 725, 726, 887]
"""

##  (g) 
#calculate median order fill
med=ff['secs'].groupby(ff['storenum']).median().to_frame()
#calculate mean median
mean_med=ff['secs'].groupby(ff['storenum']).median().mean()
#calculate standard deviation of mean
sd_med=ff['secs'].groupby(ff['storenum']).median().std(ddof=1)
#calculate bound
ubound2=mean_med+sd_med*2
lbound2=mean_med-sd_med*2
#high performance
high_med=med[med['secs']<lbound2].index
high_med
#low performance
low_med=med[med['secs']>ubound2].index
low_med
#find intersection
pd.Series(list(set(high_mean.to_series()).intersection(set(high_med.to_series())))).sort_values()
pd.Series(list(set(low_mean.to_series()).intersection(set(low_med.to_series())))).sort_values()
"""
1(g)
high performance: [27, 243, 312, 722]
low performance: [ 14,  59, 130, 149, 161, 173, 200, 233, 240, 242, 267, 290, 304,
            318, 320, 365, 402, 438, 448, 452, 478, 517, 528, 531, 546, 568,
            611, 640, 657, 702, 718, 723, 725, 726, 755, 796, 875, 887]
high performance intersection:
27, 243, 312, 722
low performance intersection:
59, 149, 233, 318, 402, 452, 528, 657, 718, 723, 725, 726, 887
"""

#### Part 2
##
fff = pd.read_csv('fastfood3.csv')

##  (a) 
#highest
len(fff[fff['satisfaction']==fff['satisfaction'].max()])/len(fff)*100
#lowest
len(fff[fff['satisfaction']==fff['satisfaction'].min()])/len(fff)*100
"""
2(a)
percentage of highest: 0.0012962667517549457=0.1296266751754946%
percentage of lowest: 4.985641352903638e-05=0.004985641352903638%
"""

##  (b)
#group by dayofweek, calculate mean of satisfaction
fff['satisfaction'].groupby(fff['dayofweek']).mean()
"""
2(b)
Fri     6.116154
Mon     6.132017
Thur    6.118582
Tues    6.142121
Wed     6.141752
"""

##  (c) 
#breakfast
#calculate proportion
phat=len(fff[(fff['meal']=="Breakfast")&(fff['satisfaction']>=7)])/len(fff[fff['meal']=="Breakfast"])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(fff[fff['meal']=="Breakfast"]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(fff[fff['meal']=="Breakfast"]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.543993358907 0.561704411531
#lunch
#calculate proportion
phat=len(fff[(fff['meal']=="Lunch")&(fff['satisfaction']>=7)])/len(fff[fff['meal']=="Lunch"])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(fff[fff['meal']=="Lunch"]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(fff[fff['meal']=="Lunch"]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.358767231898 0.367048872039
#dinner
#calculate proportion
phat=len(fff[(fff['meal']=="Dinner")&(fff['satisfaction']>=7)])/len(fff[fff['meal']=="Dinner"])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(fff[fff['meal']=="Dinner"]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(fff[fff['meal']=="Dinner"]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.433035250248 0.443232721273
"""
2(c)
Breakfast: (0.543993358907 0.561704411531)
Lunch: (0.358767231898 0.367048872039)
Dinner: (0.433035250248 0.443232721273)
"""

##  (d) 
#<=180
#calculate proportion
phat=len(fff[(fff['secs']<=180)&(fff['satisfaction']>=7)])/len(fff[fff['secs']<=180])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(fff[fff['secs']<=180]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(fff[fff['secs']<=180]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.532174605186 0.540387392872
#>=360
#calculate proportion
phat=len(fff[(fff['secs']>=360)&(fff['satisfaction']>=7)])/len(fff[fff['secs']>=360])
phat
#calculate confidence interval
lb=phat-1.96*np.sqrt(phat*(1-phat)/len(fff[fff['secs']>=360]))
ub=phat+1.96*np.sqrt(phat*(1-phat)/len(fff[fff['secs']>=360]))
#calculate CI using phat +- 1.96*sqrt(p(1-p)/n)
print(lb,ub)
#0.477593418676 0.484427890304
"""
2(d)
<=180: (0.532174605186 0.540387392872)
<=360: (0.102436119547 0.111396228888)
"""

##  (e) 
#create new column
fff['predsatis']=""
for i in range(len(fff)):
    m=0
    if fff.loc[i,'meal']=="Breakfast":
        m=1                               #value of m depends on breakfast
    fff.loc[i,'predsatis']=4+0.002*fff.loc[i,'cost']-0.005*fff.loc[i,'secs']+m
fff['predsatis'].mean()
"""
2(e)
3.8585125139598668
"""

##  (f) 
#create new column
fff['difference']=""
for i in range(len(fff)):
    fff.loc[i,'difference']=fff.loc[i,'predsatis']-fff.loc[i,'satisfaction']
    if fff.loc[i,'difference']<0:
        fff.loc[i,'difference']=-fff.loc[i,'difference'] #get absolute value
fff['difference'].max()
fff['difference'].min()
fff['difference'].mean()
"""
2(f)
max: 4.8960000000000008
min: 0.0
mean: 2.2728987017390274
"""