# Class and Object is parts of oops concepts. Earlier we did functional and procedural programming
# like lambda etc..
# Class we call call it design or blueprint of the project or object
# Object we call it instance, to create an object we have to create class
# An object have two things one is Attribute or Variables and one is behaviour
# An attribute is a data and behaviour we can say Methods or functions

class Computer:
    def config(self):
        print("i5","16gb")

com1 = Computer() # here i created an object of computer

Computer.config(com1)
# Whenever we have to call method in the class we have to use classname.methodname
# And after that pass the object there
# Here self is an object which we are passing as an argument
# Another way to use object

com1.config()