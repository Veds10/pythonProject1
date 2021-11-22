# a=1  #global variable
#
# def print_Number():
#
#             a=a+1;
#             print(a)
#
#  print_number()

# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
print(x)

# it will always look for local var 1st and will print and if local is not there then it will go for global




