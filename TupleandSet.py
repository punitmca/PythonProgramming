# Tuple is same as list but difference is that Tuple is immutable
# To add the value in tuple we will use round brackets but to fetch the value will use square brackets
# Tuple have only two values one is Index and second is Count

tup = (2,45,3,2,4)
print(tup)
print(tup[1])

# Set is collection unique elements, we will use curly brackets, In set we can not fetch the value by indexing
# Because in element is not is sequence of order but yes we can change the value

s ={2,45,6,7,43,75,77}
print(s)
# discard method is used to eliminate the particular value
s.discard(45)
print(s)
