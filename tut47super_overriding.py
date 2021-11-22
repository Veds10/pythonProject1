class A:
    classvar1="i am a class variable in class A"
    def __init__(self): # its nothin but the constructor
        print("i am a's cons")
        self.var1="i am inside class A's constructor"
        self.classvar1="instance variable in class A"
        self.special="special of A"
# after fun is overridden and want access to new instance var then use super key word

class B(A):
    classvar1 = "i am a class variable in class B"

    # def __init__(self):# its nothin but the constructor
    #     super().__init__()  #it will give b's const
    #     self.var1 = "i am inside class B's constructor"
    #     self.classvar1 = "instance variable in class B"
    #    # super().__init__() # it will give a's const which instance var
    #     print(super().classvar1) # it will give you the class variable
    #

    def __init__(self):
        super().__init__()
        print("i am b cons") # it will call b's part but if you want to print both a as well as b then just write super kw

#first it will check for instance var and then for class var

a=A()
b=B()

print(b.special, b.var1,b.classvar1)

# method resolution order is mro which goes from left to right which means if there c has a , b as parent class and if you give super kw in c then it will have access for a instead of b
