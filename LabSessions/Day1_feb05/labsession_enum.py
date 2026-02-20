#Q1

a=list(enumerate(['a', 'b', 'c']))
print(a)
#-------------------    #Q2----------------------------------------

nums=[10,20,30]
for index,num in enumerate(nums):
    print(index,num)

#---------------Q3----------------------------

colors=["red","green","blue"]
for i,color in enumerate(colors,1):
    print(i,color)

    #-----------------Q4-----------------------

a=list(enumerate("PYTHON",1))
print(a)


#---------------------Q5-------------------

nums=[10,20,30,40,50,60]
for i,ch in enumerate(nums):
    if ch==50:
        print(i)

#--------------------Q6---------------------

for i ,n in enumerate(range(10,60,10)):
    print(i,n)

#-------------------Q7--------------------

for i,n in enumerate(range(len(data))):
