# classes - template
# objects - instance/variables of class(objects are derived from class)
# dry- do not repeat

# class Student: # class var
#     pass
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"  # instance var
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)

# instance variables and class variables
class Employee:
    no_of_leaves = 8 # class var # its nothing but the attributes-variables
    pass

harry  = Employee() # its nothong but the behaviour-methods(functions) and harry rohan are the objects of the emp class
rohan = Employee()

harry.name = "Harry" # instance varv
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee._dict_)
Employee.no_of_leaves = 9
print(Employee._dict_)
print(Employee.no_of_leaves)






