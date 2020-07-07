nums = [25, 12,19,2]
print(nums)
print(nums[0])
print(nums[-1])
# In list we can put any type of data, List is mutable means we can change the data
names =['Punit', 'Nanda']
print(names)

mil = nums + names
mil1 = [nums,names]
print(mil)
print(mil1)
# In append it will insert in the last of the element
nums.append(77)
print(nums)
# By using insert we can also add the value using index
nums.insert(2, 75)
print(nums)
# Remove method used to delete particular values from the list
nums.remove(75)
print(nums)
# Pop method used for to delete the element from the list at particular position
nums.pop(0)
print(nums)
# del function is used to delete the values from any position
del nums[2:]
print(nums)
# Extend method is used for to add multiple values in the list
nums.extend([25,77,75,89,99])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)