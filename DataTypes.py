# In python we have None, Numeric, List, Set, Tuple, String, Range, Dictionary or Map
# In python we use none insted of null
# In Numeric we have int, float, complex and bool
# List, Set, Tuple, String, Range in python is called sequence

num = 6+9j
print(type(num))
a= 5.6
b= int(a)
print(type(b))
print(b)
print(range(10))
print(list(range(10)))
# If want to get even number from list range we will do like
print(list(range(2,10,2)))
# dictionary or map
d= {'Punit':'iPhone', 'Nisha':'OnePlus'}
print(d)
print(d.keys())
print(d.values())
print(d['Punit'])
print(d.get('Nisha'))