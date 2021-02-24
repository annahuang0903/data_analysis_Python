## File: yh5sc-assignment07.py 
## Topic: Assignment 07 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

import pandas as pd # load pandas as pd
import re
import operator

#Preliminary steps and data transformation
#read in file
lines = pd.Series(open('pizza_requests.txt').read().splitlines())
#reorganize the txt file into a data frame
#create column list
cols = []
i = 0
while(i<45): #45 lines per record
    result = re.search(r'\"[a-zA-Z_]+\",',lines.iloc[i]) #search for column name
    if result:
        cols.append(result.group(0).replace('"',"").replace(',',""))
        #group(0) gives the matched result, replace "" and , with null 
    i+=1;
    if re.search(r'\%{5,}', lines.iloc[i]):
    #if hit the end of record, break
        print("Found break")
        break
#set up data frame, initialize column names
df = pd.DataFrame(index= range(5671),columns=cols)
line_num = 0
i = 0
for i in range(0,5671):
    col_num = 0
    #while not contain % and line does not exceed line size
    while(line_num < lines.size and not re.search(r'\%{5,}', lines.iloc[line_num])):
        val = ""
        #the filed consists of more than one line
        if(re.search(r'\,\s\{', lines.iloc[line_num])):
            if(re.search(r'\}',lines.iloc[line_num])):
                df.iloc[i][col_num] = ""
                col_num += 1
                line_num += 1
                continue
            #while } is not identified
            line_num += 1
            while(not re.search(r'\}',lines.iloc[line_num])):
                val = val+lines.iloc[line_num].strip().replace('"',"")+","
                line_num+=1
            df.iloc[i][col_num] = val
            col_num+=1
            line_num+=1
        #each line contains a field of the record
        else:
            #append value to column number
            arr = lines.iloc[line_num].split(",")
            val=""
            #case when the text does not include more than one comma, i.e. "<Title>", <val>
            if(len(arr)==2):
                val = arr[1].strip()
            #case when the text does contain more than one comma
            else:
                #concat. all the text that is not part of the variable name
                for j in range(1,len(arr)):
                    val = val+ arr[j].strip() + ", "
            df.iloc[i][col_num] = val
            col_num+=1
            line_num+=1
    line_num+=2  #skip two lines of %%%%%%%%%
#now all data is stored in a data frame

#Questions    
#1
#divide number of true 'requester_received_pizza' by number of all
len(df[df['requester_received_pizza']=="true"])/len(df['requester_received_pizza'])
"""
#1
0.24634103332745547
"""

#2
#calculate median of 'requester_account_age_in_days_at_request'
med=df['requester_account_age_in_days_at_request'].median()
med
"""
#2
155.6475925925926
"""

#3
#calculate the proportion of successful requests among older accounts
#divide receive true and older accounts by all older account
n1=len(df[(pd.to_numeric(df['requester_account_age_in_days_at_request'])>med)])
p1=len(df[(df['requester_received_pizza']=="true")&(pd.to_numeric(df['requester_account_age_in_days_at_request'])>med)])/n1
#same for newer accounts
n2=len(df[(pd.to_numeric(df['requester_account_age_in_days_at_request'])<=med)])
p2=len(df[(df['requester_received_pizza']=="true")&(pd.to_numeric(df['requester_account_age_in_days_at_request'])<=med)])/n2
#calculate confidence interval
lb=p1-p2-1.96*(p1*(1-p1)/n1+p2*(1-p2)/n2)**(0.5)
ub=p1-p2+1.96*(p1*(1-p1)/n1+p2*(1-p2)/n2)**(0.5)
print(lb,ub)
"""
#3
(0.021770947082183623, 0.06657068220914004)
"""

#4  
#obtain lower case of request_text
df2=pd.Series(df['request_text']).str.lower()
#sum student and children together
ct=len(df2[(df2.str.contains("children")) | (df2.str.contains("student"))])
#calculate percentage
ct/len(df)*100
"""
#4
9.222359372244753%
"""

#5
#obtain lower case of request_title
df3=pd.Series(df['request_title']).str.lower()
#count number of rows with "canada"
ct=df3.str.contains("canada").sum()        
ct
"""
#5
103
"""

#6
#subset successful requests
success=df[df['requester_received_pizza']=="true"]
#count number of request_title containing N/A
ct=pd.Series(success['giver_username_if_known']).str.count('"N/A"').sum()
#calculate proportion
p=ct/len(success)
#calculate confidence interval
lb=p-1.96*(p*(1-p)/len(success))**(0.5)
ub=p+1.96*(p*(1-p)/len(success))**(0.5)
print(lb,ub)
"""
#6
(0.6899672049777826 0.7373771042562903)
"""

#7
#calculate max number of 'requester_number_of_subreddits_at_request'
pd.to_numeric(df['requester_number_of_subreddits_at_request']).max()
"""
#7
235
"""

#8  
dict={}
for i in range(len(df)):
    #if not empty
    if df['requester_subreddits_at_request'].loc[i] !="":
        #split by ","
        list=df['requester_subreddits_at_request'].loc[i].split(",")
        #create dictionary key-value pair
        for k in range(len(list)):
            if list[k]!="" and list[k] not in dict:
                dict[list[k]]=1
            elif list[k]!="" and list[k] in dict:
                dict[list[k]]+=1
#sort dictionary by value in descending order
sorted_dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
sorted_dict[0:10]
#write dictionary to file
fh = open('yh5sc-assignment07-subreddits.txt', 'w')
for i in sorted_dict:
    fh.write(str(i)+"\n")
fh.close()
"""
#8
'AskReddit', 3241,
'pics', 2734,
'funny', 2704,
'IAmA', 2138,
'WTF', 2133,
'gaming', 2079,
'Random_Acts_Of_Pizza', 1978,
'videos', 1620,
'todayilearned', 1556,
'AdviceAnimals', 1452
"""
