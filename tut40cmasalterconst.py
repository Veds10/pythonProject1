#
# class Employee:
#     no_of_leaves = 8 # class variables
#
#     def __init__(self,aname,asalary,arole): # this func gives refrence of instance variables
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod # is used to give refrence of class variables  insted of instance variables
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves=newleaves
#
#     @classmethod
#     def frm_str(cls,string): # cls is nothing but the employee class
#         # sepa= string.split("-")
#         # print(sepa)
#         # return cls(sepa[0],sepa[1],sepa[2])
#         return cls(*string.split("-"))
#
#     @staticmethod # is used to access neither class nor instance variable just to print something
#     def printgood(string):
#         print('this is good' , string) # , is given for space in sentence and + is to join the sentence
#         return"very good" # if there is no return value then it will give nonee
#
# harry = Employee("Harry",786,"teacher") #instance variable
# rohan = Employee("Rohan",456,"student")
# karan=Employee.frm_str("karan-777-stud")

#
# print(karan.printgood("wow"))

# print(karan.name)
# print(karan.salary)
#
# Employee.change_leaves(55) # class as well as instance can change the val of class using this dec methods
# rohan.change_leaves(66) # it will not get added as a instance


