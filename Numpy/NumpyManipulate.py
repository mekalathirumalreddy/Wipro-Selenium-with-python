
import numpy as np


# changing shape
# reshape

a = np.arange(1,7)
print("Original array", a)
# reshape the array
reshaped = a.reshape(2, 3)
print(reshaped)

# flat = return 1D iterator over the array
arr = np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

# flatten - Returns a copy of the array collapsed into one dimension
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

# ravel() - Returns a flattened array
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

# pad() - Returns a padded array with shape increased according to pad_width
arr = np.array([1,2,3])
padded = np.pad(arr, 3, mode= 'constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)

#Joining arrays
#concatenate() - joining 2 arrays

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b), 0))
print(np.concatenate((a,b), 1))

# stack - join the arrays along the new axis
#Adds a new dimension
#All arrays must have the same shape

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack((a,b), 0))
print(np.stack((a,b), 1))

# hstack - Stacks arrays horizontally (column-wise)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.hstack((a,b)))
print(np.concatenate((a,b), 1))

#vstack() - stacks arrays vertically(row-wise)
print(np.vstack((a,b)))
print(np.concatenate((a,b), 0))

#column stack() - stacks 1D arrays as columns into a 2D array

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))

#row stack() - stack arrays row-wise

print(np.vstack((a,b)))

# Splitting arrays
#split arrays into multiple sub-arrays based on axis
#array must be divisible equally
arr = np.array([1,2,3,4,5,6])

result = np.split(arr, 3)
print(result)

#hsplit() - Splits array horizontally (column-wise)
#Works on 2D arrays

arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])

print(np.hsplit(arr2, 2))

#Vsplit() Splits array vertically (row-wise)

arr2 = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8]])

print(np.vsplit(arr2, 2))

# Adding / Removing Elements

#resize() -Returns a new array with a specified shape
arr = np.array([1,2,3,4])
new_arr = np.resize(arr, (2,3))
print(new_arr)

# the elements will repeat in the new array
# returns a new array

# append() - Appends values at the end of an array
arr = np.array([1,2,3])
new_arr = np.append(arr, [4,5])
print(new_arr)

#2D array
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
np.append(a, b, axis=0)

#Inserts values before given index
arr = np.array([10,20,30])
new_arr = np.insert(arr, 2, 15)
print(new_arr)

# Delete elements along a specified axis
arr = np.array([10,20,30])
new_arr = np.delete(arr, 2,)
print(new_arr)

#Unique()
arr = np.array([1,2,2,3,4,4,5])
print(np.unique(arr))

#Repeating
#repeat() is used to repeat  each element of an array a specified number of times
#Each element is repeated twice
arr = np.array([10, 20, 30])
print(np.repeat(arr, 3))

#Differnt Repeats for Each element
arr = np.array([10, 20, 30])
print(np.repeat(arr, [1,2,3]))

# repeat in 2d array
arr2 = np.array([[1,2],
                 [3,4]])
print(np.repeat(arr2, 2, axis=0))

#title() The input array that will be repeated
my_array = np.array([1, 2, 3])
tiled_array = np.tile(my_array, 2)
print("Original Array:", my_array)
print("Tiled Array:", tiled_array)

# flip() -Reverse the order of elements along a given axis

#if axis = None - reverse entire flattened array
#if axis = 0 - reverse rows
#if axis =1 - reverse columns

arr = np.array([1,2,3,4])
print(np.flip(arr))

#2D
arr2 = np.array([[1,2],
                [3,4]])
print(np.flip(arr2, axis=0)) # Flip rows
print(np.flip(arr2, axis=1)) # Flip columns

#fliplr() - Flip Left-Right (axis=1) - Works only on 2D+ arrays.

arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(np.fliplr(arr2))

#flipud - Flip UP-DOWN
print(np.flipud(arr2))

# roll() -ROlls (rotates) elements along a given axis
arr2 = np.array([[1,2,3],
                 [4,5,6]])
np.roll(arr2, 2, axis=None)

#sorting and searching
#sort() - returns a sorted copy of an array (or sorts in place if using ndarray method)
arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)


#argsort() returns the indices that would sirt the array return the in dex positions
arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)
indices = np.argsort(arr)
print(indices)

#lexsort() - used ofr sorting with multiple columns(like sorting by last name, then firstname
#sort by a first
#then by b (secondary key)
#sorting happens form right to left
a = np.array([1, 1, 0, 0])
b = np.array([1, 0, 1, 0])
result = np.lexsort((b, a))
print(result)