# for loops
#
# list=[["monica",6], ["rachel",5], ["joey",4], ["phoebe",3], ["chandler",2], ["ross",1]]
#
# dict=dict(list)
# #print(dict)
#
# for k,no in dict.items():
#     print(f"{k} and {no}")
#
#
# list = [list,float,7,89,0,3,5,66]
# for item in list:
#     if str(item).isnumeric() and item>6:
#         print(item)

#
# for i in range(10,20,2):
#     print(i)
#
# for i in range(20,10,-1):
#     print(i)

#
# # while loops


# next prblm
# i=0
# while(i<45):
#     print(i)
#     i=i+1



# break brks it and continue skip it


#
while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break # it wont brk till the condition gets satisfied
    else:
        print("Try again!\n")

