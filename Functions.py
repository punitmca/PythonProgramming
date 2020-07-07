# in function we have to define and call the functions

def add(a,b):
    c= a+b
    return c
d =  int(input('one values to add'))
e =  int(input('two values to add'))
f=print(add(d,e))

def add_sub(x,y):
    c= x+y
    d= x-y
    return c,d
e =  int(input('one values to add'))
f =  int(input('two values to add'))
result,result1=add_sub(e,f)
print(result,result1)
