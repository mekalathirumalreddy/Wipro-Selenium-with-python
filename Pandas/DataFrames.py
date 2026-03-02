#DataFrame is a 2-Dimesional labeled data structure (rows & columns),
#like an Excel SQL tables
import numpy as np
import pandas as pd
#create DataFrame from List of Dictionaries

data =[
    {"name":"Ram","Age":25},
    {"name":"Sam","Age":30},
    {"name":"John","Age":28}
]
df = pd.DataFrame(data)
print(df)

#create Dataframe dictionary of series
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])

df = pd.DataFrame({"A":s1,"B":s2})
print(df)

#create Dataframe using Numpy array

import numpy as np

arr =np.array([[1,2],[3,4],[5,6]])
df =pd.DataFrame(arr,columns=["A","b"])
print(df)

#create  data from using csv file
#df = pd.read_csv("employees.csv")
#print(df)

#create empty dataframe
df = pd.DataFrame()
print(df)

#create dataframe withcustom index

data={
    "Name":["Ram","Sam"],
    "Age":[25,30]
}
df = pd.DataFrame(data,index=["Emp1","Emp2"])
print(df)

























