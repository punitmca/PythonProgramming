def update(x):
    print(id(x))
    x=8;
    print(id(x))
    print('x',x)
# Note:- before updating the value the address of x and y is same
# After updating its has been changed, in python we don't use call by value and call by reference
# The add is not changed because its a int and immutable
a=10
print(id(a))
update(a)
print("a",a)

def updates(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print('x',lst)

lst = [5,15,30]
print(id(lst))
updates(lst)
print('lst',lst)

# here lists are mutable