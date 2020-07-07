a= 10

def something():
    a = 9

    #x= globals()['a']
    print('in function', a)
    globals()['a']=15
something()
print('outside function', a)

# Note we used glbals() keyword because we want use local varibale as well global var too