from numpy import *

arr = array([
             [1,3,4,5],
             [2,4,6,8]

])
print(arr.dtype)
# dtype is funtion to give te type of the value

print(arr.ndim)
# ndim will give the dimension of the array

print(arr.shape)
# shape will give the rows and column of the array in tuple

print(arr.size)
# size will give the entire size of the array

arr1 = arr.flatten()
print(arr1)
# flattern is a funtion to covert 2d array into 1d array

arr2 = arr1.reshape(2,2,2)
print(arr2)
# reshape wil give you the new shape of array