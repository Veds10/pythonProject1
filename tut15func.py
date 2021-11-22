# function is nothing but creating formula to use it again and again

# a = 9
# b = 8
# c = sum((a, b)) # built in function
"""
def function1():
    print("hello everyone")
function1()
function1()
"""


#
def function2(a,b): # formal arguments
    """this is docstring""" # always used inside the func
    average= a+b/2
    print(average)
#     return average
# v=function2(2,7) # actual arguments
# print(v)
# print(function2.__doc__)
#
# # if you want to add multiple values by passin only one,two formal argument use * which is variable argyment
# you can also use this with string

#
# def num(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#     return c
#
#
# i=num(2,3,4,5)
# print(i)
#
# # or
#
#
# def num(*b):
#     c=0
#     for i in b:
#         c=c+i
#     return c
#
#
# i=num(2,3,4)
# print(i)
#
# # for string
#
# # def person(**data):
# #     data=data
# #     return data
# #
# # a=person(name="ved",age="21",mob="123456")
# # print(a)
#
# # or
#
#
# def person(**data):
#     data=data
#
#     for i,j in data.items(): # when u wanna fetch one by one use for and when there are keywords mandatory to use item()
#         print(i,j)
#
#
# a=person(name="ved",age="21",mob="123456")
# print(a)




# def num(a,b):
#     y=a+b
#     return y
#
# w=num(2,3)
# print(w)

 # or

#
# def num(a,b):
#     y=a+b
#     print(y)
# num(3,3)
#

