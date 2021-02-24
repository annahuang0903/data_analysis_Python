## File: yh5sc-assignment01-group3.py 
## Topic: Assignment 01 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

#### Assignment 1, Part A
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]

## A1.
print((2**521-1)%10000)
"""
#A1
7151
"""

## A2.
print(mylist01[6]*mylist01[12]*mylist02[3])
"""
#A2
-75
"""

## A3.
print(mylist02[4:9])
"""
#A3
[-5, -2, 4, 6, 7]
"""

## A4.
mylist12=mylist01+mylist02
mylist12.sort()
print(mylist12[7:19])
"""
#A4
[-3, -3, -2, -2, 0, 0, 1, 2, 2, 2, 3, 3]
"""

## A5. 
mylist12.count(8)
"""
#A5
3
"""

## A6.
mylist01_new=[]
for i in mylist01:
    if i!=3:
        mylist01_new.append(i)
print(mylist01_new)
"""
#A6
[2, 5, 4, 9, 10, -3, 5, 5, -8, 0, 2, 8, 8, -2, -4, 0, 6]
"""

## A7. 
print(mylist02[::-3])
"""
#A7
[1, 13, 9, 6, -5, -3]
"""

## A8.
mylist12=mylist01+mylist02
print(mylist12[2:][::5])
"""
#A8
[4, 5, 3, 0, -5, 7, 13]
"""

#%%

#### Assignment 1, Part B
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]

## B1. 
sum=0
for i in mylist01:
    sum=sum+i**3
print(sum)
"""
#B1
2867
"""

## B2.
mylist03=[0]*15
for i in range(15):
    mylist03[i]=mylist01[i]*mylist02[i]
print(mylist03)
"""
#B2
[-14, -15, 32, -45, -50, 6, 20, 30, 21, -40, 0, 20, 6, 104, -96]
"""

## B3. 
sum=0
for i in mylist02:
    sum=sum+i
print(sum/len(mylist02))
"""
#B3
1.588235294117647
"""

#%%

#### Assignment 1, Part C
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]
mylist03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = mylist01 + mylist02 + mylist03

## C1. 
greater=0
for i in biglist:
    if i>4:
        greater=greater+1
print(greater)
"""
#C1
23
"""

## C2. 
between=0
for i in biglist:
    if i>=-1 and i<=3:
        between=between+1
print(between)
"""
#C2
15
"""

## C3. 
mylist04=[]
for i in biglist:
    if i%3!=0:
        mylist04.append(i)
print(mylist04)
"""
#C3
[2, 5, 4, 10, 5, 5, -8, 2, 8, 8, -2, -4, -7, 8, -5, -5, -2, 4, 7, 5, 10, 2, 13, 
-4, 1, 2, -5, 7, -2, 2, 8, 7, 2, -2, 5, 5]
"""

