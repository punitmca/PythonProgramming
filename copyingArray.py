from numpy import *

# numpy is used for multidimesional array

arr = array([2,4,5,6,7])
arr1 = array([3,5,6,3,2])

arr3= concatenate([arr, arr1])
print(arr3)

arr2 = array([2,4,5,6])
arr4= arr2.view()

# view is a function to create a new array its also called shallow copy
# because i am changing in array2 but reflect in another one also
print(arr2)
print(arr4)
arr2[1]=7
print(arr2)
print(arr4)
arr5 = array([2,4,5,6])
arr6= arr5.copy()
arr5[3]=7
print(arr5)
print(arr6)
# copy is a function to also create a new array its also called deep copy