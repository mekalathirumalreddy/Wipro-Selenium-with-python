#1.Write a Python function to sum all the numbers in a list.

def b(list):
    a=0
    for i in list:
        a+=i
    return a
a=[1,2,3,4]
print(b(a))

#2.Write a Python function to find the maximum of three numbers.


def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print(max(10,200,3))
