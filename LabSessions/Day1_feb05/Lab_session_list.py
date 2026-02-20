# 1.Write a Python program to get the largest number from a list.

#[1,2,3,4,5,6,7,8,9]
a=[1,2,30,4,5,6,7,8,9]
b=len(a)
c=0
for i in range(1,b):
    if a[i]>c:
        c=a[i]
print(c)

#remove the even numbers from the list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=[]
for i in numbers:
    if i%2!=0:
        a=a+[i]
print(a)



#3.multiply the items in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=1
for i in numbers:
    a*=i
print(a)