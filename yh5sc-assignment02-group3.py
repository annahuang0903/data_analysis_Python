## File: yh5sc-assignment02.py 
## Topic: Assignment 02 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

#### Assignment 2, Part A
##
import numpy as np
## A1.
x=np.random.uniform(low=0,high=20,size=10000)
ct=0
for xval in x:
    if xval>=5 and xval<=12:
        ct+=1
print(ct/10000*100)
"""
#A1
34.88
"""

## A2. 
ctarray=np.zeros(500)
for i in range(500):
    x=np.random.uniform(low=0,high=20,size=10000)
    ct=0
    for xval in x:
        if xval>=5 and xval<=12:
            ct+=1
    ctarray[i]=ct/10000*100
print(np.mean(ctarray))
"""
#A2
34.96968
"""

## A3.
ct=1
s=np.random.choice(x,size=1)
while s>=4:
    ct+=1
    s=np.random.choice(x,size=1)
print(ct)
"""
#A3
5
"""

## A4. 
ctarray=np.zeros(1000)
for i in range(1000):
    ct=1
    s=np.random.choice(x,size=1)
    while s>=4:
        ct+=1
        s=np.random.choice(x,size=1)
    ctarray[i]=ct
print(np.mean(ctarray))
"""
#A4
5.149
"""

## A5. 
ct=0
exceed=0
while exceed<3:
    s=np.random.choice(x,size=1)
    ct+=1
    if s>12:
        exceed+=1
print(ct)
"""
#A5
8
"""

## A6.
ctarray=np.zeros(1000)
for i in range(1000):
    ct=0
    exceed=0
    while exceed<3:
        s=np.random.choice(x,size=1)
        ct+=1
        if s>12:
            exceed+=1
    ctarray[i]=ct
print(np.mean(ctarray))
"""
#A6
7.366
"""

#%%

#### Assignment 2, Part B

import numpy as np 
p1 = np.random.normal(40,12,size=500000)

#  a) 
#
#  i) 
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=10)
    xbar=np.mean(sample)
    lb=xbar-1.96*12/np.sqrt(10)
    ub=xbar+1.96*12/np.sqrt(10)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(a)(i)
0.9485
"""
    
#
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=20)
    xbar=np.mean(sample)
    lb=xbar-1.96*12/np.sqrt(20)
    ub=xbar+1.96*12/np.sqrt(20)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(a)(ii)
0.949
"""

# 
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=30)
    xbar=np.mean(sample)
    lb=xbar-1.96*12/np.sqrt(30)
    ub=xbar+1.96*12/np.sqrt(30)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(a)(iii)
0.9506
"""

#
#  b) 
#
#  i)
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=10)
    xbar=np.mean(sample)
    stdev=np.std(sample,ddof=1)
    lb=xbar-1.96*stdev/np.sqrt(10)
    ub=xbar+1.96*stdev/np.sqrt(10)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(b)(i)
0.9214
"""
    
#   ii) 
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=20)
    xbar=np.mean(sample)
    stdev=np.std(sample,ddof=1)
    lb=xbar-1.96*stdev/np.sqrt(20)
    ub=xbar+1.96*stdev/np.sqrt(20)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(b)(ii)
0.9338
"""

#   iii) 
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=30)
    xbar=np.mean(sample)
    stdev=np.std(sample,ddof=1)
    lb=xbar-1.96*stdev/np.sqrt(30)
    ub=xbar+1.96*stdev/np.sqrt(30)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(b)(iii)
0.9424
"""
#
#  c) 
#
#  i)
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=10)
    xbar=np.mean(sample)
    stdev=np.std(sample,ddof=1)
    lb=xbar-2.262*stdev/np.sqrt(10)
    ub=xbar+2.262*stdev/np.sqrt(10)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(c)(i)
0.9529
"""
    
#   ii) 
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=20)
    xbar=np.mean(sample)
    stdev=np.std(sample,ddof=1)
    lb=xbar-2.093*stdev/np.sqrt(20)
    ub=xbar+2.093*stdev/np.sqrt(20)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(c)(ii)
0.9496
"""

#   iii) 
ct=0
for i in range(10000):
    sample=np.random.choice(p1,size=30)
    xbar=np.mean(sample)
    stdev=np.std(sample,ddof=1)
    lb=xbar-2.045*stdev/np.sqrt(30)
    ub=xbar+2.045*stdev/np.sqrt(30)
    if lb<=40 and ub>=40:
        ct+=1
print(ct/10000)
"""
#B(c)(iii)
0.9514
"""








