import numpy as np
import pandas as pd
'''

Creating data

Selecting data

Filtering data

Cleaning data

Transforming columns

Aggregating data

Merging datasets

Exporting results
'''
#creating Data DFR using dictionary
data ={
    "Name":["Ram","Sam","John","Priya"],
    "Age":[25,30,28,22],
    "salary":[40000,50000,45000,38000]
}

df = pd.DataFrame(data)
print(df)

#selecting single data
print(df["Age"])
#selecting multiple data or columns

print(df[["Age","Name"]])
#select rows using iloc or loc

print(df.loc[0:2]) #nth index
print(df.iloc[0:1]) # n-1 index

#filtering based on the condition
df = pd.DataFrame(data)
print(df)

#employees with salary >40000
filtered = df[df["salary"]>40000]
print(filtered)
filtered=df[df["salary"]<=40000]
print(filtered)

#multiple conditions
filtered=df[(df["salary"]>40000) & (df["Age"]>25)]
print(filtered)

#Cleaning data - adding or modifying the columns
data={
    "Name":["Ram","Sam","John"],
    "salary":[40000,50000,45000]
}
df =pd.DataFrame(data)
#add the bonus coulumn
df["Bonus"] =df["salary"]*0.10
print(df)

#modify the current column - increase the salary
df["salary"]=df["salary"]+2000
print(df)


#sorting Data ascending or descending

data ={
    "Name":["Ram","Sam","John","Priya"],
    "Age":[25,30,28,22],
    "salary":[40000,50000,45000,38000]
}
df = pd.DataFrame(data)
#sort the salary in ascending order
sorted_df = df.sort_values("salary",ascending=False)
print(sorted_df)

#hanlding missing value
data ={
    "Name":["Ram","Sam",None],
    "Age":[25,np.nan,30]
}
df =pd.DataFrame(data)
print("missing values")
print(df.isnull())

#replace all missing values (Nan,None,NoT) in the DataFrame with 0
#drop missing rows
df_filled = df.fillna(0)
print(df_filled)

data={
    "Age":[25,None,30],
    "salary":[50000,60000,None]
}
df = pd.DataFrame(data)
print(df)
df = df.fillna(0)
print(df)
#drop missing rows
data={
    "Name":["A","B","C"],
    "Age":[25,None,30],
    "salary":[5000,60000,None]
}
#groupBy and Aggregation

data ={
    "city":["Delhi","Mumbai","Delhi","Chennai"],
    "salary":[40000,50000,45000,38000]
}
df=pd.DataFrame(data)
#average salary per city
result = df.groupby("city")["salary"].mean()
print(result)

#multiple aggregation
result=df.groupby("city")["salary"].agg(["mean","sum","count"])
print(result)

#Merging DataFrames

df1=pd.DataFrame({
    "ID":[1,2],
    "Name":["Ram","Sam"]
})

df2=pd.DataFrame({
    "ID":[1,2],
    "salary":[40000,50000,40000]
})
merged = pd.merge(df1,df2,on="ID",how="inner")
print(merged)
#removing Duplicates
data={
    "Name":["Ram","Sam","Ram"],
    "Salary":[40000,50000,40000]
}
print("Before removing duplicates:")
print(df)
df = df.drop_duplicates()
print("After removing duplicates:")
print(df)

