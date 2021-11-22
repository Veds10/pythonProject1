# def function1():
#     print("subscribe now")
#
# func=function1
# del function1 # it will not get deleted unless the fun is func
# func()


# def funcret(num):   # whenever you use if with func insted pf print use return
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=funcret(1)
# print(a)

# def executor(func):
#     func ("this")
#
# executor(print)

  #orr
#
# def executor(func):
#      return("this")
#
# a=executor("this")
# print(a)


#decorators

def inner1(func):
    def inner2():
        print("Before function execution");
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function")

function_to_be_used()


# eg



def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_harry():
    print("Harry is a good boy")  # if you use print insted pf return just call the func and it eill give o/p but if u use return then save that fun in somethinf and then print that somethin

# who_is_harry = dec1(who_is_harry)

who_is_harry()




