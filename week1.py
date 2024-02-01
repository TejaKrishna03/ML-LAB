# Write a Pandas program to convert Series of lists to one Series.


import pandas as pd
import numpy as np
s = pd.Series([1,2,3,np.nan,5,6], index=['A','B','C','D','E','F'])
print(s)

#

df1 = pd.Series([23,45,65,32,43,44,34,43])

print(df1[df1%2==0])

#

df1 = pd.Series([78,98,56,76,32,78,98,78])
a=df1.mode()[0]
df1[df1!=a]='other'
print(df1)

#

df1 = pd.Series([5,10,64,60,34,54])

print(df1[df1%5==0].index)

#

df2 = pd.Series(['Hi','Hello','How',"World",'Python'])

for i in df2:
    print(i,len(i))


#
    
from dateutil.parser import parse
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("Original Series:")
print(date_series)
print("\nNew dates:")
result = date_series.map(lambda d: parse('11 ' + d))
print(result)

#

dict1 = {
    'Students':['Jim',"Dwight","Pam","John","Tony"],
    'Age':[19,19,19,20,19],
    'Marks':[230,235,260,270,220],
    'Out of':[300,300,300,300,300]
}

ds = pd.DataFrame(dict1,index=['Student1','Student2','Student3','Student4','Student5'])
ds

#

dict1 = {
    'Students':['Jim',"Dwight","Pam","John","Tony"],
    'Age':[19,19,19,20,19],
    'Marks':[230,235,260,270,220],
    'Out of':[300,300,300,300,300],
    'No of Attempts':[1,2,1,3,3]
}
ds1 = pd.DataFrame(dict1)

print(ds1[ds1['No of Attempts']>2])

# 

dict1 = {
    'Students':['Jim',"Dwight","Pam","John","Tony"],
    'Age':[19,19,19,20,19],
    'Marks':[230,235,120,270,100],
    'Out of':[300,300,300,300,300]
}
df4 = pd.DataFrame(dict1)

df4['k'] = [54,43,54,64,32]

print(df4)

df4.drop(['k'],axis=1)
print(df4)

# 

dict1 = {
    'Names':['Jim',"Dwight","Pam","John","Tony"],
    'Age':[19,19,19,20,19],
    'Score':[230,235,120,270,100],
    'Out of':[300,300,300,300,300],
}

df3 = pd.DataFrame(dict1)

df3 = df3.sort_values(['Names','Score'],ascending=[False,True])

print(df3)

#


dict1 = {
    'Students':['Jim',"Dwight","Pam","John","Tony"],
    'Age':[19,19,19,20,19],
    'Marks':[230,235,120,270,100],
    'Out of':[300,300,300,300,300],
    'Qualify':['Yes','Yes','No','Yes','No']
}

ds2 = pd.DataFrame(dict1)

ds2['Qualify']= ds2['Qualify'].replace({'Yes':True,'No': False})
print(ds2)

#

dict2 = {
    'X':[21,32,45,67,np.inf],
    'Y':[32,54,np.inf,98,89]
}

ds3 = pd.DataFrame(dict2)

ds3 = ds3.replace({np.inf:np.NaN})

ds3 = ds3.dropna()
print(ds3)