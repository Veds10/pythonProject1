# overloading and Dunder

# all the methos starting and endin with __ are called as a dunder methods init is one of them and also its a constructor






class Employee:
    no_of_leaves = 8

    def _init_(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def _add_(self, other):
        return self.salary + other.salary

    def _truediv_(self, other):
        return self.salary / other.salary

    def _repr_(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def _str_(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))

# watch the vi