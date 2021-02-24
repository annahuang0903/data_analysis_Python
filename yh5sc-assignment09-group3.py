## File: yh5sc-assignment09.py 
## Topic: Assignment 09 Solutions
## Name: Yehan Huang
## Section time: 2:00-3:15
## Grading Group: 3

#1
import pandas as pd # load pandas as pd
import numpy as np
import re
reviews = pd.read_csv('reviews.txt', 
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date'])
#Find the 5 reviewers index with the most reviews
top5=reviews['Reviewer'].value_counts().sort_values(ascending=False).iloc[0:5].index
#average rating of top5
reviews1=reviews[reviews['Reviewer'].isin(top5)]['Rating']
avg1=reviews1.mean()
#average rating of non top5
reviews2=reviews[~reviews['Reviewer'].isin(top5)]['Rating']
avg2=reviews2.mean()
#CI for avg1
lb=avg1-1.96*np.std(reviews1,ddof=1)/np.sqrt(len(reviews1))
ub=avg1+1.96*np.std(reviews1,ddof=1)/np.sqrt(len(reviews1))
print(lb,ub)
avg2
"""
1.
95% CI: 2.90485863509 2.9975803893
average rating for remainder: 3.5484703356591387
It is not in top5 CI.
"""

#2
#read in genres
genres = pd.read_csv('genres.txt', 
                        sep='|',
                        header=None,
                        names=['Movie', 'movie title', 'release date', 'video release date',
	'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation',
	'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
	'FilmNoir', 'Horror', 'Musical', 'Mystery', 'Romance', 'SciFi',
	'Thriller',  'War', 'Western'])
#merge with reviews
df1=pd.merge(genres,reviews)
#get top 10 with most reviews
df1['movie title'].value_counts().iloc[0:10]
"""
2.
Star Wars (1977)                 583
Contact (1997)                   509
Fargo (1996)                     508
Return of the Jedi (1983)        507
Liar Liar (1997)                 485
English Patient, The (1996)      481
Scream (1996)                    478
Toy Story (1995)                 452
Air Force One (1997)             431
Independence Day (ID4) (1996)    429
"""

#3
#sum up number of each genre
df1.loc[:,'Action':'Western'].sum(axis=0).sort_values()
"""
3.
most: Drama          39895
least: Documentary      758
"""

#4
#sum up number of genres of each movie
df1['num genres']=df1.loc[:,'Action':'Western'].sum(axis=1)
#calculate proportion of at least 2 genres over all reviews
df1[df1['num genres']>=2]['Movie'].nunique()/df1['Movie'].nunique()*100
"""
4.
50.4756242568371%
"""

#5
#read in reviewers
reviewers = pd.read_csv('reviewers.txt', 
                        sep='|',
                        header=None,
                        names=['Reviewer','age','gender','occupation','zip code'])
#merge with reviews
df2=pd.merge(reviewers,reviews)
#male average
df2m=df2[df2['gender']=="M"]['Rating']
avgm=df2m.mean()
#calculate CI
lbm=avgm-1.96*np.std(df2m,ddof=1)/np.sqrt(len(df2m))
ubm=avgm+1.96*np.std(df2m,ddof=1)/np.sqrt(len(df2m))
print(lbm,ubm)
#female average
df2f=df2[df2['gender']=="F"]['Rating']
avgf=df2f.mean()
#calculate CI
lbf=avgf-1.96*np.std(df2f,ddof=1)/np.sqrt(len(df2f))
ubf=avgf+1.96*np.std(df2f,ddof=1)/np.sqrt(len(df2f))
print(lbf,ubf)
"""
5.
male: 3.52130852808 3.53726944122
female: 3.517202288 3.54581247502
"""

#6
#Create a Series 'zipseries' that has zip codes as the index, and the corresponding state or territory as the values.
zips = pd.read_csv('zipcodes.txt',    # Read in zip codes, eliminate dups
                  usecols = [1,4],
                  converters={'Zipcode':str}).drop_duplicates()
zipseries = pd.Series(data=zips['State'].values, index=zips['Zipcode'])
#Define a function that takes a string as input and returns one of 'Canada', 'Unknown', or a state/territory code.
def ziptostate(zcode):
    if re.search('[a-zA-Z]+', zcode):
        return('Canada')
    elif zcode in zipseries.index:
        return(zipseries[zcode])
    else:
        return('Unknown')
#Use '.apply' to run each reviewer's zip code through 'ziptostate' then use the resulting Series as a new column for 'reviewers.txt'
df2['location'] = df2['zip code'].apply(ziptostate)
#count values and get top 10
df2['location'].value_counts()[0:10]
""""
6.
CA    13842
MN     7635
NY     6882
IL     5740
TX     5042
OH     3475
PA     3339
MD     2739
VA     2590
MA     2584
"""

#7
#group rating by occupation and sort values
df2['Rating'].groupby(df2['occupation']).mean().sort_values()
"""
7.
highest: lawyer           3.735316
lowest: healthcare       2.896220
"""

#8
#count number of reviews
ct=df1['Movie'].groupby(df1['Movie']).count().sort_values()
#new data frame
df3=pd.Series.to_frame(reviews['Movie'].groupby(ct).count())
#compute percentage
df3['percentage']=df3['Movie']/df1['Movie'].nunique()*100
#get top 20
df3['percentage'][0:20]
"""
8.
1.0     8.382878
2.0     4.042806
3.0     3.567182
4.0     3.804994
5.0     3.032105
6.0     2.318668
7.0     2.615933
8.0     1.783591
9.0     1.961950
10.0    1.961950
11.0    1.189061
12.0    1.664685
13.0    1.486326
14.0    0.832342
15.0    1.307967
16.0    1.129608
17.0    0.594530
18.0    1.426873
19.0    1.070155
20.0    0.713436
"""

#9
#create column of genres
genre=['Action', 'Adventure', 'Animation','Childrens', 'Comedy', 'Crime', 
       'Documentary', 'Drama', 'Fantasy','FilmNoir', 'Horror', 'Musical', 
       'Mystery', 'Romance', 'SciFi','Thriller',  'War', 'Western']
#create column of sum of rating
sum=[0]*18
#create column of count of rating
count=[0]*18
#loop through dataframe and calculate sum and count
for i in range(len(df1)):
    for j in range(len(genre)):
        if df1.iloc[i].iloc[j+6]==1:
            count[j]+=1
            sum[j]+=df1.iloc[i].iloc[25]
df4=pd.concat([pd.Series(genre), pd.Series(sum),pd.Series(count)], axis=1)
df4['average']=df4[1]/df4[2]
df4['average'].sort_values()
"""
9.
highest: FilmNoir    3.921523
lowest: Fantasy    3.215237
"""

#10
#(a)
#all female rating
df2female=df2[df2['gender']=="F"]
#positive female rating
df2femalep=df2[(df2['gender']=="F") & (df2['Rating']>=4)]
#female proportion
pf=len(df2femalep)/len(df2female)
#all male rating
df2male=df2[df2['gender']=="M"]
#positive male rating
df2malep=df2[(df2['gender']=="M") & (df2['Rating']>=4)]
#male proportion
pm=len(df2malep)/len(df2male)
#calculate CI
lb1=(pf-pm)-1.96*(pf*(1-pf)/len(df2female)+pm*(1-pm)/len(df2male))**(0.5)
ub1=(pf-pm)+1.96*(pf*(1-pf)/len(df2female)+pm*(1-pm)/len(df2male))**(0.5)
print(lb1,ub1)
"""
10(a)
-0.005765857971269032 0.008326737855068527
"""

#(b)
#all canadian rating
df2c=df2[df2['location']=="Canada"]
#positive canadian rating
df2cp=df2[(df2['location']=="Canada") & (df2['Rating']>=4)]
#canadian proportion
pc=len(df2cp)/len(df2c)
#all american rating
df2a=df2[(df2['location']!="Canada")&(df2['location']!="Unknown")]
#positive american rating
df2ap=df2[(df2['location']!="Canada")&(df2['location']!="Unknown") & (df2['Rating']>=4)]
#american proportion
pa=len(df2ap)/len(df2a)
#calculate CI
lb2=(pc-pa)-1.96*(pc*(1-pc)/len(df2c)+pa*(1-pa)/len(df2a))**(0.5)
ub2=(pc-pa)+1.96*(pc*(1-pc)/len(df2c)+pa*(1-pa)/len(df2a))**(0.5)
print(lb2,ub2)
"""
10(b)
-0.0694173743938817 -0.02605023995043969
"""
