# class Employee:
#     def __init__(self,ffname,llname):
#         self.fname=ffname
#         self.lname=llname
#        # self.email=f"{self.fname}{self.lname}@gmail.com"
#
#     def explain(self):
#         return f"this is {self.fname} {self.lname}"
#
#     @property # decorator u can directly call without using ()
#     def email(self):
#         return f"{self.fname}{self.lname}@gmail.com"
#
#
#  # to create obj/instance var
#
# abc=Employee("vedanti","saraf")
# xyz=Employee("khushi","varma")
#
# #print(abc.email)
#
# # to change the name of objects setter is used
#
# abc.fname="ved"
# print(abc.email)


class Employee:
    def _init_(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property # getter
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter # setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)

del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)