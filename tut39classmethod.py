
class Employee:
    no_of_leaves = 8 # class or static variables they are same
    # but class meth and static meth are different we use static when we are neither concerned with class nor instance diff from this both

    def __init__(self,aname,asalary,arole): # this func gives refrence of instance variables
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod # is used to give reference of class variables  instead of instance variables
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves



harry = Employee("Harry",786,"teacher") #instance variable
rohan = Employee("Rohan",456,"student")


Employee.change_leaves(55) # class as well as instance can change the val of class using this dec methods
rohan.change_leaves(66) # it will not get added as a instance
print(Employee.no_of_leaves)

print (harry.printdetails())
print (rohan.printdetails())

