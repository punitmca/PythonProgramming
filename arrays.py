from array import *

vals= array('i',[5,9,8,4,2])

print(vals.buffer_info())
# in buffer_info output we get two values one is address and one is size
vals.reverse()
print(vals)

for i in range(len(vals)):
    print(vals[i])
# create new array
newArr = array(vals.typecode,(j*j for j in vals))
# here typecode is used for to know the type of  values and after that it will take one value and one by one
# assigned in array
# if we want to print square of the values just use *
for i in newArr:
    print(i)

