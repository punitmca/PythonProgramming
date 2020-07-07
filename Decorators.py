# In python we can use decorators when we want to add more features in our existing function

def div(a,b):
    print(a/b)

def new_div(func):
    def swap_div(a,b):
        if a<b:
            a,b= b,a
            return func(a,b)
    return swap_div

div1 = new_div(div)
div1(2,4)
