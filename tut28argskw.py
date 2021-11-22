
# # def function_name_print(a, b, c, d, e):
# #     print(a, b, c, d, e)
#
# def funargs(normal, *argsrohan, **kwargsbala):
#     print(normal)
#     for item in argsrohan:
#         print(item)
#     print("\nNow I would Like to introduce some of our heroes")
#     for key, value in kwargsbala.items():
#         print(f"{key} is a {value}")
#
#
# # function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")
#
# har = ["Harry", "Rohan", "Skillf", "Hammad",
#        "Shivam", "The programmer"]
# normal = "I am a normal Argument and the students are:"
# kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
#       "The Programmer": "Coordinator", "Shivam":"Cook"}
# funargs(normal, *har, **kw)

# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)

# function_name_print("ved","khu","dev","nai","dis")



def funcargs(*args,**kwargs):
    for item in list:
        print(f" items are {item}")
    for key,values in dict.items(): #whenever if u just want to print key that time name of the list is ok but for values too youhave to give items()
        # print(key,"is a",values)
        print(f"{key} is a {values}")


list=["abc","qwe","azs","cdf","bhj","yui","opl"]
dict={"rohan":"artist","ron":"actor","naruto":"favourite"}

funcargs(*list,*dict)