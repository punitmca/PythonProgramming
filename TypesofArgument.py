def person(name, age):
    print(name)
    print(age)
# whatever we write in () are called arguments, In python there are two type of arguments
# one is Formal which we used in define and one is actual where we given a name and age
# Actual argument have 4 types of arguments
# Position, Keyword, default, and Variable length

person(age=30,name ="punit")
# here we are using keyword of name and age
# suppose if we want to use default argument
def person(name, age=18):
    print(name)
    print(age)
person("punit")
# let see if we are not giving any value in the time of actual argument it used default value
# if we give the value it will override the value let see the below example
person("Punit", 30)

# Now will see the last argument type which is Variable Length
# Variable Length we use where length is not fixed

def sum(a, *b):

    c = a
    for i in b:
        c= c + i
    print(c)
sum(1,2,3,4,5)
# Note: we are using here loop to add the values because b is coming in tuple
# so I am fetching one by one value from tuple and add them



