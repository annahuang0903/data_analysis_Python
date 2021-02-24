## File: yh5sc-assignment06.py 
## Topic: Assignment 06 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

lines = open('timing_log.txt').read().splitlines()
import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
# 1. 
#count number of lines containing "hardcopy"
ct = 0
for aline in lines:
    if aline.count("hardcopy") >0: 
        ct += 1
print(ct)
"""
#1
138
"""

# 2. 
#count number of lines containing "STAT2120"
ct = 0
for aline in lines:
    if aline.count("STAT2120") > 0:
        ct += 1
#divide by all lines
ct/len(lines)*100
"""
#2
percentage: 52.49243925331108 %
"""

# 3. 
#count number of lines with webwork section containing only 2 elements
list1=[]
ct = 0
for aline in lines:
    if len(aline.split("/")) == 3:
        if aline.split("/")[2].split()[0]!="]":
            list1.append(aline.split("[")[2])
            ct += 1
    elif len(aline.split("/")) == 4:
         if aline.split("/")[3].split()[0]=="]":
            list1.append(aline.split("[")[2])
            ct += 1
#divide by all lines
ct/len(lines)*100
"""
#3
percentage: 3.792105537595161 %
"""

# 4. 
ct = 0
for aline in lines:
    if len(aline.split("[")[2].split("/")) > 3:
    #check if the webwork section has more than 2 elements
        if aline.split("[")[2].split("/")[3].count("instructor")>0:
    #obtain number of lines in which the 3rd position of webwork is instructor
            ct += 1
ct
"""
#4
388
"""

# 5. 
#new list store value of hours of each line
hours=[]
for aline in lines:
    hour=aline.split("]")[0].split(" ")[3].split(":")[0] #obtain hour
    hours.append(hour) #append hour of each line to the list
pd.Series(hours).value_counts()  #calculate counts of each hour
#max is first line: 22    6331; min is last line: 06     332
"""
#5
hour with most entries: 22
hour with least entries: 6
"""

# 6. 
#new list store value of class of each line
classes=[]
for aline in lines:
    if len(aline.split("[")[2].split("/"))>2:
    #check if out of bounds
        clas=aline.split("[")[2].split("/")[2] #obtain class
        classes.append(clas) #append class of each line to the list
len(np.unique(classes))
"""
#6
67
"""

# 7. 
#    (a) 
#count number of each class
pd.Series(classes).value_counts()
"""
#7a
Spring11-STAT2120                    30308
Spring12-STAT2120                     9213
Spring11-APMA2130-Fulgham             7553
"""

#    (b) 
runtimes=[]
#new list store value of runtime of each line
for aline in lines:
    if len(aline.split("[")[2].split("/"))>2:
    #check if the entry contains class name
        runtime=float(aline.split("] ")[2].split(" ")[2]) #obtain runtime
        runtimes.append(runtime) #append runtime
#create data frame combining class and runtime
df=pd.concat([pd.Series(classes),pd.Series(runtimes)],axis=1)
#multiply mean runtime of each class by number of each class, and sort them
(df.groupby(0).sum()).sort_values(by=1,ascending=False)

"""
#7b
Spring11-STAT2120                  5268.912
Spring11-APMA2130-Fulgham          2143.625
Spring12-APMA2130                  1286.974
"""

# 8.
#group by class, calculate mean and sort values
df.groupby(0).mean().sort_values(by=1,ascending=False)
"""
#8
APMA2120-Devel                     0.533469
apma2130-devel                     0.387673
Spring12-APMA2130                  0.362222
"""

# 9. 
#create new list to contain problems 
problems=[]
ct = 0
for aline in lines:
    if len(aline.split("[")[2].split("/")) >= 6:  #check bounds
        if(str.isdigit(aline.split("[")[2].split("/")[4])): 
        #check if this is problem number
            problems.append(aline.split("[")[2])  #append to list
            ct += 1
#divide by all lines
ct/len(lines)*100
"""
#9
percentage: 78.5079257482532%
"""

# 10. 
#calculate number of each problem and get first one
pd.Series(problems).value_counts()
"""
#10
[/webwork2/Spring11-STAT2120/Webwork09/22/]                         1215

#%%

