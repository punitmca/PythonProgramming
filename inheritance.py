class A:
   def funA(self):
    print ("function A")
    def fun(self):
        print("function A")

class B(A):
    def newFun(self):
        print("testing")

class C(A,B):
    def func(self):
        print("newtest file")

a=B()
a.newFun()
c=C()
c.

