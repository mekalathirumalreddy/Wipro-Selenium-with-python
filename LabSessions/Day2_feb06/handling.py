#file handling
#=============

#1.Write a Python program to sort a list of tuples using Lambda.

#2.Write a Python program to extract year, month, date and time using Lambda.

#3.Write a Python script to concatenate the following dictionaries to create a new one.


data = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)


import datetime

now = datetime.datetime.now()

extract = lambda d: (d.year, d.month, d.day, d.time())

result = extract(now)

print("Year, Month, Date, Time:", result)


dict1 = {1: "A", 2: "B"}
dict2 = {3: "C", 4: "D"}
dict3 = {5: "E"}
result = {}
result.update(dict1)
result.update(dict2)
result.update(dict3)

print(result)
