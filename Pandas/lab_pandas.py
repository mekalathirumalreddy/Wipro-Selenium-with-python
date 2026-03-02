#1
import pandas as pd
import numpy as np

data = {
    "Name": ["Ravi", "Anita", "John", "Meena", "Kiran"],
    "Age": [25, 30, None, 28, 22],
    "Salary": [50000, 60000, 55000, None, 45000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "City": ["Bangalore", "Hyderabad", "Bangalore", "Chennai", None]
}

df = pd.DataFrame(data)
print(df)


#2
print(df.isnull())
print(df.isnull().sum())


#3
df_filled = df.fillna(0)
print(df_filled)

#4
df_dropped = df.dropna()
print(df_dropped)

#5
df_sorted_age = df.sort_values(by="Age", ascending=True)
print(df_sorted_age)

#6
df_sorted_salary = df.sort_values(by="Salary", ascending=False)
print(df_sorted_salary)

#7
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)


#8

total_salary = df.groupby("Department")["Salary"].sum()
print(total_salary)

#9

filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print(filtered)

#10
df["Tax"] = df["Salary"].apply(lambda x: x * 0.10 if pd.notnull(x) else x)
print(df)
