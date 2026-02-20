

#1.Create a dictionary with student roll number as key and name as value. Print the dictionary.

student={
    1:"varun",
    2:"Tharun",
    3:"karun"
}
print(student)

#2.Access the value of a key that exists and one that does not exist

print(student[1])

print(student.get(5))


# 3.Update the value of an existing key in a dictionary.

student[1]="sridhar"
print(student)

#4.Delete a key from a dictionary using:
   #.del
   # .pop()

del student[1]
print(student)

student.pop(2)
print(student)

#5.Find the number of key–value pairs in a dictionary.

student={
    1:"varun",
    2:"Tharun",
    3:"karun"
}
print(len(student))

#6.Print only:
 # .keys
  # .values
   #.key–value pairs

for i in student:
    print(i)
for i in student:
    print(student[i])
for i in student:
    print(i,student[i])