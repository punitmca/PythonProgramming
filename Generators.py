# generator give you iterator
# yeild and return will work same but difference is that yeild will terminate the execution

def topfive():

    n =1
    while n<=10:
        sq= n*n
        yield sq
        sq+=1


val = topfive()
for i in val:
    print(i)