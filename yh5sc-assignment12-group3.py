## File: yh5sc-assignment12.py 
## Topic: Assignment 12 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#1
#list of age
age=list(range(40,66))
#new df
df1=pd.DataFrame()
df1['Age']=age
#list of balance
bal=[]
bal.append(50000.00)
#calculate balance for each year
for i in range(25):
    newb=bal[-1]*np.exp(0.076)
    bal.append(newb)
#round
bal=np.round(bal,2)
df1['Balance']=bal
print(df1.to_string(index=False))
"""
1.
Age    Balance
 40   50000.00
 41   53948.13
 42   58208.01
 43   62804.27
 44   67763.45
 45   73114.23
 46   78887.52
 47   85116.68
 48   91837.71
 49   99089.45
 50  106913.81
 51  115356.00
 52  124464.81
 53  134292.87
 54  144896.98
 55  156338.42
 56  168683.30
 57  182002.97
 58  196374.39
 59  211880.62
 60  228611.26
 61  246662.99
 62  266140.14
 63  287155.25
 64  309829.77
 65  334294.72
 """
 
#2
#list to hold simulation
finalbal=[]
#calculate returns
for i in range(100000):
    bal2=[]
    bal2.append(50000.00)
    for j in range(25):
        newb=bal2[-1]*np.exp(np.random.normal(0.076, 0.167))
        bal2.append(newb)
    finalbal.append(bal2[-1])
#mean balance
print("%.2f" % np.mean(finalbal)) 
#median balance
print("%.2f" % np.median(finalbal)) 
#95% confidence interval
print("%.2f" % np.percentile(finalbal,2.5),"%.2f" % np.percentile(finalbal,97.5))
#porportion of at least 300000
finalbal=pd.Series(finalbal)
len(finalbal[finalbal>=300000])/len(finalbal)
#plot histogram
plt.hist(finalbal, bins=500, range=[finalbal.min()-10000, finalbal.max()+10000])  
"""
2.
(a)
473349.56
(b)
334013.03
(c)
65081.03, 1710652.46
(d)
0.55115
(e)
see attached
"""

#3
#list of age
age=list(range(40,66))
#new df
df1=pd.DataFrame()
df1['Age']=age
#list of balance
bal=[]
bal.append(50000.00)
#calculate balance for each year
for i in range(25):
    newb=bal[-1]*np.exp(0.076)+3000
    bal.append(newb)
#round
bal=np.round(bal,2)
df1['Balance']=bal
print(df1.to_string(index=False))
"""
3.
Age    Balance
 40   50000.00
 41   56948.13
 42   64444.90
 43   72533.63
 44   81261.08
 45   90677.66
 46  100837.80
 47  111800.22
 48  123628.25
 49  136390.25
 50  150159.98
 51  165017.00
 52  181047.16
 53  198343.11
 54  217004.80
 55  237140.05
 56  258865.24
 57  282305.91
 58  307597.51
 59  334886.20
 60  364329.68
 61  396098.09
 62  430375.01
 63  467358.53
 64  507262.36
 65  550317.10
"""
 
#4
#list to hold simulation
finalbal=[]
#calculate returns
for i in range(100000):
    bal2=[]
    bal2.append(50000.00)
    for j in range(25):
        newb=bal2[-1]*np.exp(np.random.normal(0.076, 0.167))+3000
        bal2.append(newb)
    finalbal.append(bal2[-1])
#mean balance
print("%.2f" % np.mean(finalbal)) 
#median balance
print("%.2f" % np.median(finalbal)) 
#95% confidence interval
print("%.2f" % np.percentile(finalbal,2.5),"%.2f" % np.percentile(finalbal,97.5))
#porportion of at least 300000
finalbal=pd.Series(finalbal)
len(finalbal[finalbal>=300000])/len(finalbal)
#plot histogram
plt.hist(finalbal, bins=500, range=[finalbal.min()-10000, finalbal.max()+10000])  
"""
4.
(a)
744345.53
(b)
560984.01
(c)
150252.81, 2441162.96
(d)
0.81578
(e)
see attached
"""

#5
#list of age
age=list(range(40,66))
#new df
df1=pd.DataFrame()
df1['Age']=age
#list of balance
bal=[]
bal.append(50000.00)
#list of deposit
dep=[]
dep.append(3000)
#calculate balance and deposit for each year
for i in range(25):
    newb=bal[-1]*np.exp(0.076)+dep[-1]
    bal.append(newb)
    newd=dep[-1]*np.exp(0.03)
    dep.append(newd)
#round
bal=np.round(bal,2)
df1['Balance']=bal
print(df1.to_string(index=False))
"""
5.
Age    Balance
 40   50000.00
 41   56948.13
 42   64536.26
 43   72817.72
 44   81850.12
 45   91695.71
 46  102421.74
 47  114100.87
 48  126811.61
 49  140638.73
 50  155673.82
 51  172015.80
 52  189771.51
 53  209056.35
 54  229994.92
 55  252721.79
 56  277382.29
 57  304133.33
 58  333144.36
 59  364598.32
 60  398692.74
 61  435640.90
 62  475673.06
 63  519037.80
 64  566003.51
 65  616859.91
"""

#6
#list to hold simulation
finalbal=[]
#calculate returns
for i in range(100000):
    bal2=[]
    bal2.append(50000.00)
    dep2=[]
    dep2.append(3000)
    for j in range(25):
        newb=bal2[-1]*np.exp(np.random.normal(0.076, 0.167))+dep2[-1]
        bal2.append(newb)
        newd=dep2[-1]*np.exp(0.03)
        dep2.append(newd)
    finalbal.append(bal2[-1])
#mean balance
print("%.2f" % np.mean(finalbal)) 
#median balance
print("%.2f" % np.median(finalbal)) 
#95% confidence interval
print("%.2f" % np.percentile(finalbal,2.5),"%.2f" % np.percentile(finalbal,97.5))
#porportion of at least 300000
finalbal=pd.Series(finalbal)
len(finalbal[finalbal>=300000])/len(finalbal)
#plot histogram
plt.hist(finalbal, bins=500, range=[finalbal.min()-10000, finalbal.max()+10000])  
"""
6.
(a)
816780.96
(b)
630666.43
(c)
187226.57, 2526010.84
(d)
0.87461
(e)
see attached
"""

#7
#list of age
age=list(range(40,66))
#new df
df1=pd.DataFrame()
df1['Age']=age
#list of balance
bal=[]
bal.append(50000.00)
#list of deposit
dep=[]
dep.append(3000)
#calculate balance and deposit for each year
for i in range(25):
    newb=bal[-1]*np.exp(0.076)+dep[-1]
    bal.append(newb)
    newd=dep[-1]*np.exp(0.03)
    dep.append(newd)
#new age list
age2=list(range(66,101))
#new df
df2=pd.DataFrame()
df2['Age']=age2
#list of new balance
bal3=[]
bal66=bal[-1]*np.exp(0.035)-25000
bal3.append(bal66)
for i in range(34):
    newb=bal3[-1]*np.exp(0.035)-25000
    bal3.append(newb)
#round
bal3=np.round(bal3,2)
df2['Balance']=bal3
print(df2.to_string(index=False))
"""
7.
balance on 100th: 412508.87
    
Age    Balance
 66  613832.28
 67  610696.81
 68  607449.65
 69  604086.83
 70  600604.23
 71  596997.57
 72  593262.45
 73  589394.29
 74  585388.34
 75  581239.71
 76  576943.29
 77  572493.85
 78  567885.91
 79  563113.84
 80  558171.79
 81  553053.71
 82  547753.32
 83  542264.13
 84  536579.43
 85  530692.23
 86  524595.33
 87  518281.26
 88  511742.29
 89  504970.40
 90  497957.30
 91  490694.40
 92  483172.79
 93  475383.26
 94  467316.27
 95  458961.94
 96  450310.03
 97  441349.95
 98  432070.70
 99  422460.94
100  412508.87
""" 

#8
#list to hold simulation
finalbal=[]
#calculate returns
for i in range(100000):
    bal2=[]
    bal2.append(50000.00)
    dep2=[]
    dep2.append(3000)
    #before 65
    for j in range(25):
        newb=bal2[-1]*np.exp(np.random.normal(0.076, 0.167))+dep2[-1]
        bal2.append(newb)
        newd=dep2[-1]*np.exp(0.03)
        dep2.append(newd)
    bal4=[]
    bal66=bal2[-1]*np.exp(np.random.normal(0.035,0.051))-25000
    bal4.append(bal66)
    #after 65
    for k in range(34):
        newb=bal4[-1]*np.exp(np.random.normal(0.035,0.051))-25000
        bal4.append(newb)   
    finalbal.append(bal4[-1])
#mean balance
print("%.2f" % np.mean(finalbal)) 
#median balance
print("%.2f" % np.median(finalbal)) 
#95% confidence interval
print("%.2f" % np.percentile(finalbal,2.5),"%.2f" % np.percentile(finalbal,97.5))
#porportion of at least 300000
finalbal=pd.Series(finalbal)
len(finalbal[finalbal>0])/len(finalbal)
#plot histogram
plt.hist(finalbal, bins=500, range=[finalbal.min()-10000, finalbal.max()+10000])  
"""
8.
(a)
1188525.63
(b)
446800.80
(c)
-1109007.75, 7916865.91
(d)
0.63552
(e)
see attached
"""