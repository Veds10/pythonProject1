class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole): # whatever you take fun in class it will take as a self unless u give decorator,init is nothing but the
        # initialization of variables(attributes)
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        print(f"my name is { self.name } , salary is {self.salary} and role is {self.role}")


#harry=Employee()
vedanti=Employee("Vedanti",100000,"student")


# harry.name="Harry"
# harry.salary=345
# harry.role="teacher"
#
# vedanti.name="Vedanti"
# vedanti.salary=6789
# vedanti.role="student"


print(vedanti.printdetails())