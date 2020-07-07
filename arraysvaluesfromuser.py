from array import *

arr = array('i',[])

n= int(input('Please enter the length of the array'))

for i in range(n):
    x= int(input('Please enter the next values'))
    arr.append(x)
print(arr)

val = int(input('enter the values to search the index'))

k=0
for e in arr:
    if e==val:
        print(k)
    k+=1
print(arr.index(val))