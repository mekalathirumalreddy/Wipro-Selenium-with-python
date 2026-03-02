'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
    using numpy.eye()
'''

import numpy as np
from numpy.ma.core import identity

#1D array
#This function creates a Numpy array with zero
#by default , the data type is float6

a=np.zeros(5)
print(a)

#2D array Zeros
a_2D = np.zeros((2,3))
print(a_2D)

a=np.ones(5)
print(a)

#2D array ones
a_2D = np.ones((2,3))
print(a_2D)

#using numpy.arrange() Function
#The numpy.arrange() function creates an array by generating sequence of numbers based on
#it is similar to python's built-in range() function.

#providing the start,stop and step values
a=np.linspace(0,10,num=5,endpoint=True)
print(a)

#exclude the last number
a=np.linspace(0,10,num=5,endpoint=False)
print(a)

#using numpy.randeom.rand( function
#generates an array of the specified shape with randdom values between  0 and 1
#if no arguments is provided , it returns a single random float value.

a=np.random.rand(5)
print(a)

#2D

a=np.random.rand(2,3)
print(a)

#3D
a=np.random.rand(2,3,4)
print(a)

#using numpy.empty() function
#2D
#This function initializes an array without initializing its elements;
#the content of the array is arbitary and may vary
a=np.empty((2,3))
print(a)

#using numpy.full( Function
#in the following example , we are the numpy.full( function to create a 2-dimensional
#filled entirely with the value

a=np.full((2,3),5)
print(a)

#numpy.eye()
#The Numpy eye() function is used to
#vreate a 2D array with ones on the diagonal and zeros in all other positions
identity_matrix = np.eye((4))
print(identity_matrix)

#numpy.identity - function is used generate a square identity matrix
identity_matrix = np.identity((5))
print(identity_matrix)

#numpy.diag
#in case of 2D array,the function extracts the diagonal elements of the array.
#in case of 1D array the function creates a square diagonal matrix with the elements of the
#the diagonal values and zeros in remaining positions

matrix =np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Original matrix",matrix)

Diagonal_elements=np.diag(matrix)
print("Diagonal elements",Diagonal_elements)