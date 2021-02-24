
## File: yh5sc-assignment10.py 
## Topic: Assignment 10 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

#1
import pandas as pd
import glob # 'glob' searches for files
# '*.csv' selects files ending in '.csv'
filelist = glob.glob('*.csv') # 'glob.glob'
# We can concatenate the dataframes into one large dataframe
df = pd.DataFrame()
for f in filelist:
    newdf = pd.read_csv(f)
    newdf['Name']=f.split(".")[0]
    df = pd.concat([df,newdf])
#mean for the Open, High, Low, and Close entries for all of the records 
df['Open'].mean()
df['High'].mean()
df['Low'].mean()
df['Close'].mean()
"""
1.
Open: 50.86385220906213
High: 51.459411725747884
Low: 50.25336771426483
Close: 50.876481580135426
"""

#2
#group Close by Name and calculate average, convert to Series
#top 5
pd.Series(df['Close'].groupby(df['Name']).mean().sort_values(ascending=False)).iloc[0:5]
#bottom 5
pd.Series(df['Close'].groupby(df['Name']).mean().sort_values()).iloc[0:5]
"""
2.
top 5:
CME     253.956017
AZO     235.951950
AMZN    185.140534
BLK     164.069088
GS      139.146781

bottom 5:
FTR      8.969515
F       11.174158
XRX     11.291864
ETFC    12.808103
HBAN    13.697483
"""

#3
#new column for volatility
df['Volatility']=df['High']-df['Low']
#group Volatility by Name and calculate average, convert to Series
#top 5
pd.Series(df['Volatility'].groupby(df['Name']).mean().sort_values(ascending=False)).iloc[0:5]
#bottom 5
pd.Series(df['Volatility'].groupby(df['Name']).mean().sort_values()).iloc[0:5]
"""
3.
top 5:
CME     7.697287
AMZN    4.691407
BLK     4.470693
AZO     4.330294
ICE     4.056189

bottom 5:
FTR     0.205275
XRX     0.308743
F       0.323567
HBAN    0.343893
NI      0.363250
"""

#4
#new column for volatility2
df['Volatility2']=(df['High']-df['Low'])/(0.5*(df['Open']+df['Close']))
#group Volatility2 by Name and calculate average, convert to Series
#top 5
pd.Series(df['Volatility2'].groupby(df['Name']).mean().sort_values(ascending=False)).iloc[0:5]
#bottom 5
pd.Series(df['Volatility2'].groupby(df['Name']).mean().sort_values()).iloc[0:5]
"""
4.
top 5:
AAL     0.055533
LVLT    0.054870
EQIX    0.051295
REGN    0.048172
ETFC    0.045381

bottom 5:
GIS    0.013966
PG     0.014192
K      0.014992
CL     0.015521
WEC    0.015761
"""

#5
#convert Date type
df['Date'] = pd.to_datetime(df['Date']) 
#subset all 2010 February
df2=df[(df['Date'].dt.month==2)&(df['Date'].dt.year==2010)]
#find the average daily price for all stocks for each of Open, High, Low, Close, and Volume
df2['Open'].mean()
df2['High'].mean()
df2['Low'].mean()
df2['Close'].mean()
df2['Volume'].mean()
"""
5.
Open: 42.695302612334764
High: 43.2036726447041
Low: 42.20083026584948
Close: 42.80405956540884
Volume: 7416516.797548362
"""

#6
#subset all 2012
df3=df[df['Date'].dt.year==2012]
#group by Date and calculate mean volatility and sort values
df3['Volatility2'].groupby(df3['Date']).mean().sort_values()
"""
6.
max: 2012-06-21    0.033606
min: 2012-12-24    0.013579
"""

#7
#subset all 2008-2013
year=[2008,2009,2010,2011,2012,2013]
df4=df[df['Date'].dt.year.isin(year)]
#extract day of week
df4['datofweek']=df4['Date'].dt.weekday_name
#group by day of week and calculate mean volatility and sort values
df4['Volatility2'].groupby(df4['datofweek']).mean()
"""
7.
Monday       0.028542
Tuesday      0.029436
Wednesday    0.029766
Thursday     0.031066
Friday       0.029041
"""

#8.
#subset all 2010 October
df5=df[(df['Date'].dt.month==10)&(df['Date'].dt.year==2010)]
#new df to hold results
df6=pd.DataFrame()
#Find Volume sum of each day
vol=df5['Volume'].groupby(df5['Date']).sum()
#new columns in df5 to hold products
df5['OpenPI']=df5['Open']*df5['Volume']
df5['HighPI']=df5['High']*df5['Volume']
df5['LowPI']=df5['Low']*df5['Volume']
df5['ClosePI']=df5['Close']*df5['Volume']
#group product by date, find Python index for each,  and paste to df6
df6['Open']=df5['OpenPI'].groupby(df5['Date']).sum()/vol
df6['High']=df5['HighPI'].groupby(df5['Date']).sum()/vol
df6['Low']=df5['LowPI'].groupby(df5['Date']).sum()/vol
df6['Close']=df5['ClosePI'].groupby(df5['Date']).sum()/vol
#print
df6
"""
8.
                 Open       High        Low      Close
Date                                                  
2010-10-01  39.272779  39.540464  38.574467  38.961689
2010-10-04  36.513664  36.973598  36.039906  36.473198
2010-10-05  36.868819  37.448798  36.515236  37.154517
2010-10-06  40.069422  40.526281  38.790438  39.453984
2010-10-07  38.738979  38.982299  38.023149  38.494185
2010-10-08  33.953131  34.418515  33.601610  34.141493
2010-10-11  36.415035  36.840357  35.996804  36.331342
2010-10-12  36.550699  37.148552  36.185750  36.956121
2010-10-13  36.769845  37.277431  36.410377  36.830507
2010-10-14  31.929174  32.188759  31.399433  31.746258
2010-10-15  31.379396  31.574286  30.611508  31.058207
2010-10-18  34.735203  35.208943  34.389509  34.947873
2010-10-19  33.418144  33.812511  32.833834  33.171654
2010-10-20  33.225863  33.908320  32.849706  33.555329
2010-10-21  40.968005  41.634092  40.219655  40.945613
2010-10-22  40.206448  40.821101  39.843407  40.424731
2010-10-25  35.196479  35.525335  34.779042  35.002647
2010-10-26  37.425957  38.443149  37.176602  38.095958
2010-10-27  40.800620  41.430831  40.293345  40.981265
2010-10-28  38.377249  38.645428  37.617353  38.085284
2010-10-29  40.159713  40.638799  39.741861  40.279059
"""