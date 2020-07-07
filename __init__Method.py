class Computer:
    def __init__(self, cpu,ram):
        self.cpu= cpu
        self.ram= ram

    def config(self):
        print("Confing is ",self.cpu,self.ram)

com1 = Computer('i5',16)
com2 = Computer('i7',32)
com1.config()
com2.config()

# __init__ here is to intialize the variables,its a constructor
# now in this every object has its own value