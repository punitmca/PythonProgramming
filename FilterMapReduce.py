from functools import reduce

nums =[2,4,6,7,8,9,3,11]

evens =list(filter(lambda n:n%2==0, nums))

print(evens)

doubles = list(map(lambda n:n*2, evens))
print(doubles)

sum = reduce(lambda a,b:a+b, doubles)
print(sum)