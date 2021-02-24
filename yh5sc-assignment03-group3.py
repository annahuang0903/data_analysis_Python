## File: yh5sc-assignment03.py 
## Topic: Assignment 03 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

#### Assignment 3, Part A

import numpy as np # Load NumPy
arr1 = np.array([[2,5,3,-1,0,1,-6,8,1,-9],[-1,3,4,2,0,1,2,7,8,-1],
                [3,0,-2,-2,5,4,8,-1,0,2],[3,3,-3,2,4,5,1,9,8,6],
                [1,1,0,2,-3,-2,4,-7,0,-9],[0,1,7,8,-5,-4,0,2,5,-9]])

##  (a) 
arr1_slice1=arr1[1:3,]
print(arr1_slice1)
"""
#A(a)
[[-1  3  4 ...,  7  8 -1]
 [ 3  0 -2 ..., -1  0  2]]
"""

##  (b) 
print(arr1[arr1<-5])
"""
#A(b)
[-6 -9 -7 -9 -9]
"""

##  (c) 
print((arr1>3).sum())
"""
#A(c)
17
"""

##  (d)
print(arr1[arr1<=-2].mean())
"""
#A(d)
-5.08333333333
"""

##  (e) 
print((arr1[arr1%2==0]**2).sum())
"""
#A(e)
512
"""

##  (f) 
print((arr1>3).sum()/(arr1>0).sum())
"""
#A(f)
0.472222222222
"""

#%%

#### Assignment 3, Part B
##
##

arr2 = np.arange(-20,28,2)
arr2 = arr2.reshape((4,6))
arr3 = np.arange(-20,12)
arr3 = arr3.reshape((8,4))

##  (a)
arr2_sub=arr2[[0,3]][:,[1,4]]
print(arr2_sub.mean())
print(arr2_sub.std())
"""
#B(a)
3.0
18.2482875909
"""

##  (b)
result=arr2*3+1
print(np.where(result%2==0,0,result))
"""
#B(b)
[[-59 -53 -47 -41 -35 -29]
 [-23 -17 -11  -5   1   7]
 [ 13  19  25  31  37  43]
 [ 49  55  61  67  73  79]]
"""

##  (c) 
print(arr3[[1,6],:].T)
"""
#B(c)
[[-16   4]
 [-15   5]
 [-14   6]
 [-13   7]]
"""

##  (d)
result2=np.where((arr3<0) & (arr3%2==1),0,arr3)
print(result2.mean(axis=1))
"""
#B(d)
[-9.5 -7.5 -5.5 -3.5 -1.5  1.5  5.5  9.5]
"""

##  (e) 
print(np.intersect1d(arr2,arr3))
"""
#B(e)
[-20 -18 -16 ...,   6   8  10]
"""

##  (f) 
print(np.setdiff1d(arr3,arr2))
"""
#B(f)
[-19 -17 -15 ...,   7   9  11]
"""

#%%


#### Assignment 3, Part C

## C1. 
##     
##  (i) 
def grade(avg):
    if avg>=90:
        return("A")
    elif avg>=80:
        return("B")
    elif avg>=70:
        return("C")
    elif avg>=60:
        return("D")
    elif avg<60:
        return("F")
    else:
        return("grade not valid")
##  (ii) 
avg=[99, 73, 60, 91, 93, 92, 68, 55, 60, 79, 79, 92, 51, 78, 68, 90, 99,
       62, 58, 76, 78, 65, 92, 83, 95, 82, 92, 85, 83, 65, 85, 61, 69, 72,
       63, 79, 59, 63, 85, 97]
grades=[]
for i in avg:
    grades.append(grade(i))
print(grades)
"""
#C1(ii)
['A', 'C', 'D', 'A', 'A', 'A', 'D', 'F', 'D', 'C', 'C', 'A', 'F', 'C', 'D', 
'A', 'A', 'D', 'F', 'C', 'C', 'D', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'D', 
'B', 'D', 'D', 'C', 'D', 'C', 'F', 'D', 'B', 'A']
"""


