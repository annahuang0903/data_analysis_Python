## File: yh5sc-assignment11.py 
## Topic: Assignment 11 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

import pandas as pd
import glob # 'glob' searches for files
import numpy as np
# '*.csv' selects files ending in '.csv'
filelist = glob.glob('*.csv') # 'glob.glob'
# We can concatenate the dataframes into one large dataframe
df = pd.DataFrame()
for f in filelist:
    newdf = pd.read_csv(f)
    newdf['Name']=f.split(".")[0]
    df = pd.concat([df,newdf])

#1
df['Date'] = pd.to_datetime(df['Date']) 
#subset all 2005-2014
df2=df[(df['Date'].dt.year>=2005)&(df['Date'].dt.year<=2014)]
#get unique dates
df3=pd.Series.to_frame(df2['Date'].drop_duplicates())
#extract year
df3['Year']=df3['Date'].dt.year
#group by year and count
df3.groupby('Year').count()
"""
1.
Year      
2005   252
2006   251
2007   251
2008   253
2009   252
2010   252
2011   252
2012   250
2013   252
2014   252
"""

#2
#unique names
names=df['Name'].unique()
#list of missing number
missing=[]
#list of total open dates within record range
total=[]
#list of start date
start=[]
#list of end date
end=[]
for i in names:
    #extract date for each name and record start and end date
    date=df.loc[df['Name']==i,'Date']
    start.append(date.min())
    end.append(date.max())
    #subset of open dates when there is record
    open=df3[(df3['Date']>=date.min())&(df3['Date']<=date.max())]
    total.append(len(open))
    #open date of this stock
    date2=date[(date.dt.year>=2005) & (date.dt.year<=2014)]
    #compute difference and append to list
    missing.append(len(open)-len(date2))
#compute total
pd.Series(missing).sum()
"""
2.
9459
"""

#3
#new df
df4=pd.DataFrame()
df4['Name']=names
df4['Missing']=pd.Series(missing)
df4['Start']=start
df4['End']=end
#ignore company with no record from 2005-2014
df4=df4[(df4['Start'].dt.year<=2014)&(df4['End'].dt.year>=2005)]
#sort by missing and get least 10
df4.sort_values(['Missing']).iloc[0:10,:][['Name','Missing']]
#top 10
df4.sort_values(['Missing'],ascending=False).iloc[0:10,:]
#least missing in top 10 is 42 with ties
df4[df4['Missing']>=42].sort_values(['Missing'],ascending=False)[['Name','Missing']]
"""
3.
most missing:
     Name  Missing
197  PDCO       45
100   FLR       44
232    SO       44
235   STJ       44
107    GE       43
206   PPG       43
217    RF       43
29    BBT       42
105   GAS       42
124   HOT       42
149    LB       42
156  LVLT       42
212  QCOM       42
240   SWN       42

fewest missing:
     Name  Missing
290   ZTS        0
287   XYL        0
252  TRIP        0
189  NWSA        0
183  NLSN        0
176  NAVI        0
157   LYB        0
112    GM        0
9     ADT        0
94     FB        0
"""

#4
#use the total list generated in #2
df4['Total']=pd.Series(total)
#calculate proportion
df4['Proportion']=df4['Missing']/df4['Total']
#sort by proportion
df4.sort_values(['Proportion']).iloc[0:10,:]
#least proportion is 0.0 with ties
df4[df4['Proportion']==0][['Name','Missing','Proportion']]
#top 10
df4.sort_values(['Proportion'],ascending=False).iloc[0:10,:]
##least proportion in top 10 is 0.016687 with ties
df4[df4['Proportion']>=0.016686].sort_values('Proportion',ascending=False)[['Name','Missing','Proportion']]
"""
4.
largest proportion:
     Name  Missing  Proportion
232    SO       44    0.018242
197  PDCO       45    0.017878
212  QCOM       42    0.017744
100   FLR       44    0.017481
235   STJ       44    0.017481
107    GE       43    0.017084
206   PPG       43    0.017084
217    RF       43    0.017084
108   GGP       41    0.016859
29    BBT       42    0.016687
105   GAS       42    0.016687
124   HOT       42    0.016687
149    LB       42    0.016687
156  LVLT       42    0.016687
240   SWN       42    0.016687

smallest proportion:
     Name  Missing  Proportion
9     ADT        0         0.0
94     FB        0         0.0
112    GM        0         0.0
157   LYB        0         0.0
176  NAVI        0         0.0
183  NLSN        0         0.0
189  NWSA        0         0.0
252  TRIP        0         0.0
287   XYL        0         0.0
290   ZTS        0         0.0
"""

#5
df6=pd.DataFrame()
for i in names:
    #extract date for each name
    date=df.loc[df['Name']==i,'Date']
    #subset of open dates when there is record
    open=df3[(df3['Date']>=date.min())&(df3['Date']<=date.max())]
    total.append(len(open))
    #open date of this stock
    date2=date[(date.dt.year>=2005) & (date.dt.year<=2014)]
    open=pd.Series(open['Date'])
    #obtain missing dates
    diff=np.setdiff1d(open,date2)
    #store in data frame
    df5=pd.DataFrame()
    df5['Date']=diff
    df5['Name']=i
    #concat with previous
    df6=pd.concat([df6,df5])
#group by date, count and sort
df6.groupby('Date').count().sort_values('Name',ascending=False)
"""
5.
2007-06-25    11
2012-04-23    11
2005-12-15    11
2013-01-30    10
2013-09-23    10
2011-03-08    10
2005-05-05    10
2005-07-14    10
2006-12-04    10
2005-02-28    10
"""

#6
#lists
open=[]
high=[]
low=[]
close=[]
volume=[]
current=""
for i in range(len(df6)):
    if current!=df6.iloc[i,:]['Name']:
        #subset the company
        name=df[df['Name']==df6.iloc[i,:]['Name']]
        #subset date
        date=name['Date']
        current=df6.iloc[i,:]['Name']
    #missing date
    d2=df6.iloc[i,:]['Date']
    #closest before date
    d1=date[date<=d2].iloc[0]
    #closest after date
    d3=date[date>=d2].iloc[-1]
    d4=d3-d2
    d5=d2-d1
    d6=d3-d1
    #calculate open for missing
    p1=name[(name['Date']==d1)]['Open'].iloc[0]
    p3=name[(name['Date']==d3)]['Open'].iloc[0]
    p2=(d4.days*p1+d5.days*p3)/d6.days
    #put in list
    open.append(p2)
    #calculate high for missing
    p1=name[(name['Date']==d1)]['High'].iloc[0]
    p3=name[(name['Date']==d3)]['High'].iloc[0]
    p2=(d4.days*p1+d5.days*p3)/d6.days
    #put in list
    high.append(p2)
    #calculate low for missing
    p1=name[(name['Date']==d1)]['Low'].iloc[0]
    p3=name[(name['Date']==d3)]['Low'].iloc[0]
    p2=(d4.days*p1+d5.days*p3)/d6.days
    #put in list
    low.append(p2)
    #calculate close for missing
    p1=name[(name['Date']==d1)]['Close'].iloc[0]
    p3=name[(name['Date']==d3)]['Close'].iloc[0]
    p2=(d4.days*p1+d5.days*p3)/d6.days
    #put in list
    close.append(p2)
    #calculate volume for missing
    p1=name[(name['Date']==d1)]['Volume'].iloc[0]
    p3=name[(name['Date']==d3)]['Volume'].iloc[0]
    p2=(d4.days*p1+d5.days*p3)/d6.days
    #put in list
    volume.append(p2)   
#store in df6
df6['Open']=open
df6['High']=high
df6['Low']=low
df6['Close']=close
df6['Volume']=volume
#concat with df2
df7=pd.DataFrame()
df7=df2.append(df6)

#(a)
#subset all 2010 October
df8=df7[(df7['Date'].dt.month==10)&(df7['Date'].dt.year==2010)]
#new df to hold results
df9=pd.DataFrame()
#Find Volume sum of each day
vol=df8['Volume'].groupby(df8['Date']).sum()
#new columns in df8 to hold products
df8['OpenPI']=df8['Open']*df8['Volume']
df8['HighPI']=df8['High']*df8['Volume']
df8['LowPI']=df8['Low']*df8['Volume']
df8['ClosePI']=df8['Close']*df8['Volume']
#group product by date, find Python index for each,  and paste to df9
df9['Open']=df8['OpenPI'].groupby(df8['Date']).sum()/vol
df9['High']=df8['HighPI'].groupby(df8['Date']).sum()/vol
df9['Low']=df8['LowPI'].groupby(df8['Date']).sum()/vol
df9['Close']=df8['ClosePI'].groupby(df8['Date']).sum()/vol
#print
df9
"""
6(a)
                 Open       High        Low      Close
Date                                                  
2010-10-01  39.169581  39.434530  38.461729  38.847595
2010-10-04  36.510926  36.970777  36.037449  36.470644
2010-10-05  36.821391  37.397876  36.469230  37.105123
2010-10-06  39.893535  40.348672  38.636233  39.300411
2010-10-07  38.711915  38.958309  38.004147  38.474292
2010-10-08  33.890921  34.354389  33.540042  34.078250
2010-10-11  36.729402  37.154667  36.305414  36.646461
2010-10-12  36.442557  37.035612  36.078277  36.841441
2010-10-13  36.963579  37.470745  36.601837  37.025214
2010-10-14  32.105693  32.370234  31.580260  31.928302
2010-10-15  31.384209  31.578964  30.617056  31.063536
2010-10-18  34.031321  34.490335  33.683067  34.226742
2010-10-19  33.253679  33.645777  32.673050  33.010323
2010-10-20  33.199450  33.880878  32.823187  33.527427
2010-10-21  40.940366  41.605321  40.194412  40.919451
2010-10-22  40.189095  40.802296  39.830970  40.410532
2010-10-25  35.343950  35.672289  34.925287  35.151389
2010-10-26  37.290510  38.299406  37.040847  37.953417
2010-10-27  39.112723  39.718565  38.627671  39.289454
2010-10-28  38.538390  38.825426  37.787602  38.267811
2010-10-29  39.347623  39.811310  38.935350  39.458878
"""

#(b)
#subset all 2008-2012
df10=df7[(df7['Date'].dt.year>=2008)&(df7['Date'].dt.year<=2012)]
#new df to hold results
df11=pd.DataFrame()
#Find Volume sum of each day
vol=df10['Volume'].groupby(df10['Date']).sum()
#new columns in df10 to hold products
df10['OpenPI']=df10['Open']*df10['Volume']
df10['HighPI']=df10['High']*df10['Volume']
df10['LowPI']=df10['Low']*df10['Volume']
df10['ClosePI']=df10['Close']*df10['Volume']
#group product by date, find Python index for each, and paste to df11
df11['Open']=df10['OpenPI'].groupby(df10['Date']).sum()/vol
df11['High']=df10['HighPI'].groupby(df10['Date']).sum()/vol
df11['Low']=df10['LowPI'].groupby(df10['Date']).sum()/vol
df11['Close']=df10['ClosePI'].groupby(df10['Date']).sum()/vol
#obtain time info
df11['Year']=df11.index.year
df11['Month']=df11.index.month
df11['Year-Month']=df11['Year']*100+df11['Month']
#new data frame to store group by month data
df12=pd.DataFrame()
#group by and calculate mean
open=pd.Series.to_frame(df11['Open'].groupby(df11['Year-Month']).mean())
high=pd.Series.to_frame(df11['High'].groupby(df11['Year-Month']).mean())
low=pd.Series.to_frame(df11['Low'].groupby(df11['Year-Month']).mean())
close=pd.Series.to_frame(df11['Close'].groupby(df11['Year-Month']).mean())
#join together
open.join(high).join(low).join(close)
"""
6(b)
                 Open       High        Low      Close
Year-Month                                            
200801      43.879383  44.892409  42.818134  43.879455
200802      44.312511  45.094670  43.430333  44.231277
200803      43.931635  44.795459  43.048824  43.933829
200804      44.443226  45.155724  43.795947  44.503364
200805      46.223506  46.903393  45.527736  46.240284
200806      43.551863  44.206226  42.731014  43.351498
200807      40.355927  41.309069  39.296554  40.294039
200808      41.288243  42.040213  40.513061  41.308876
200809      40.180907  41.356652  38.654772  39.998303
200810      31.236292  32.628599  29.519426  30.985339
200811      27.219452  28.183572  25.990354  27.058088
200812      26.335239  27.183410  25.544060  26.413611
200901      25.409133  26.069218  24.567002  25.308607
200902      21.604370  22.229320  20.907962  21.537163
200903      21.135608  21.857057  20.461184  21.201853
200904      23.071624  23.851243  22.531289  23.285297
200905      24.395802  25.015676  23.782373  24.428134
200906      26.374804  26.816666  25.879218  26.354770
200907      26.714240  27.212668  26.268579  26.811794
200908      28.961602  29.516990  28.487846  29.062931
200909      30.872073  31.393763  30.383100  30.899522
200910      32.438632  32.937909  31.901634  32.393257
200911      32.019869  32.471559  31.640013  32.113337
200912      32.763814  33.119627  32.400190  32.742729
201001      32.705986  33.121490  32.155696  32.608962
201002      33.132899  33.590305  32.712490  33.230161
201003      34.026824  34.439033  33.705850  34.099288
201004      36.493883  36.989883  35.956138  36.493005
201005      34.991162  35.602147  34.217451  34.919117
201006      34.969566  35.442337  34.399057  34.854441
201007      33.607538  34.101586  33.069073  33.652820
201008      35.069629  35.561742  34.632379  35.129022
201009      36.286588  36.778156  35.907844  36.384822
201010      36.660515  37.134589  36.135863  36.666509
201011      37.720691  38.234390  37.284057  37.807793
201012      39.662716  40.081944  39.251770  39.684723
201101      39.626213  40.106999  39.128459  39.667586
201102      42.111608  42.680693  41.621860  42.212864
201103      42.638494  43.186795  42.078523  42.651902
201104      42.867418  43.353457  42.320513  42.860279
201105      42.486394  42.965594  41.996559  42.498843
201106      39.442939  39.915710  38.998463  39.428882
201107      42.172371  42.731904  41.674772  42.201682
201108      34.352679  35.003856  33.486768  34.211051
201109      37.009378  37.650239  36.107664  36.725012
201110      34.838146  35.551106  34.138827  34.922552
201111      34.096725  34.566951  33.503721  34.019407
201112      33.602081  34.031428  33.111160  33.537572
201201      36.615057  37.266753  36.128494  36.824483
201202      37.729617  38.218533  37.302312  37.801535
201203      36.854072  37.273991  36.465473  36.917044
201204      38.646941  39.105297  38.166190  38.629491
201205      36.616235  37.099327  36.010804  36.460415
201206      35.507085  35.974332  35.038382  35.539954
201207      37.884296  38.400811  37.362617  37.910984
201208      37.160381  37.574388  36.803358  37.204773
201209      37.713443  38.147519  37.328751  37.760984
201210      38.252714  38.763395  37.739419  38.242168
201211      36.931831  37.411101  36.523875  36.988903
201212      37.350130  37.825887  36.975137  37.443758
"""
