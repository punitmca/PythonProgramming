x = 3
r = x % 2

if r==0:
    print("even number")
    if x>5:
        print("Great")
    else:
        print("Not great")
else:
    print("odd number")
if x==1:
    print("one")
# elif function will work when first will not true
elif x==2:
    print("two")
elif x==3:
    print("three")
elif x==4:
    print("four")
else:
    print("wrong input")