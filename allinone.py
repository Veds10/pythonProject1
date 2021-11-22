# 1
# print ("hello world")

# 2 calculator
# on command prompt

# 3 comments

# for single line cooment

'''
multi line
comments
'''

# use of end=""
# print("subscribe now","to me",end="")
# print("subscribe now","to me")# by default , gives space
# print("next line")


# escape sequence char \n \t
#
# print("E:\\neda") # \n new line so to print it use \\
# print("E:\"neda\"") # using "" in ""
# print("veda is  \n good girl \t")

# 4 variables ,datatypes
#
# var1="veda saraf" # str
# var2="welcome"    # str
# var3=56           # int
# var4=1.5          # float

# here + will be use as addition for no and will join/concatenate the str
# print((var1 +" " + var2))
#
# print(type(var2)) # type gives us datatype
#
# print((var3+ var4))

# typecast it converts one datatype to other one
#
# int()
# str()
# float()
#
# var1="10" # str
# var2="5"  # str
#
# print(int(var1)+int(var2))
#
# print(10*"helllo world \n")





# 5 input by user using input
# whenever you use input it takes as a string

# , gives bydefault space but + not
# out=input("enter your no")
# print("you enter",int(out)+10)
# print("you enter"+out)

# simple calculator
#
# a=int(input("num 1"))
# b=int(input("num 2"))
#
# print("add",a+b)
# print("sub",a-b)
# print("mul",a*b)
# print("div",a/b)



# 6 string  slicing index val starts with o but count is from 1-n

# mystr="veda is good girl"
# print(mystr[0:17]) # extracting subpart
# print(len(mystr))
#
# print(mystr[0:17:2])# skips the letter orr
# print(mystr[::2])
#
# print(mystr[0:]) # will take rest of the str
# print(mystr[:7]) # will take 0 bydefault

# negative slicing
# print(mystr[-4:-2])
# print(mystr[::-1]) # will give mirror view
# print(mystr[::-2])# will give mirror view and will skip


# some functions of str
#
# mystr = "happy birthday to you"
# print(mystr.isalnum())
#
# print(mystr.endswith("ou"))
# print(mystr.count("o"))
# print(mystr.capitalize())
# print(mystr.replace("you","i"))
# print(mystr.find("birthday"))
# print(mystr.lower())
# print(mystr.upper())


# 7 list functions []

"""
grocery = ["vegies","maggi","biscuits","choco",56]
print (grocery[0])
print (grocery[0:4]) #slice fun
"""
#mutable = can change for instance lists we use square [] for it
# numbers = [11,20,3,41,25,6]
# numbers.sort()
# numbers.reverse()
# numbers.append(90) # adds no at the end
# numbers.insert(2,8)
# numbers.remove(8)
# numbers.pop()
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))



#immutable = cant change for instance tuples we use parenthesis () with tuples
#
# tp=(1,2,3) # we cant add sort append etc to tuples
#
# print(tp)
#
# # to swap numbers
#
# a=1
# b=5
#
# a,b=b,a
# print(a,b)
#


# 8 {} for dictionary , [] for list, () for tuple

# Dictionary is nothing but key value pairs
# d1 = {}
# print(type(d1))
#
# d2 = {"Harry":"Burger",
#       "Rohan":"Fish",
#       "SkillF":"Roti",
#       "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
#
# d2["Ankit"] = "Junk Food"
# print(d2)
# d2[420] = "Kebabs"
# print(d2)
# # del d2[420]
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())
#
# data ={1:"ved",2:"khush",3:"dev"}
# print(data)
#
# print(data[1])# extracting val with the help of keys
# print(data.get(2))
#
# keys=["navin","kiran","harsh"]
# values=["python","java","js"]
# data1=dict(zip(keys,values)) # zip is used to merge no of lists into dict
# print(data1)
# data1["sam"]="c"
# data1.update({"ved":"py"})
# print(data1 )


# eg dict

# try:
#     dict={"beam": "to smile",
#             "furious": "angry",
#             "starving": "hungry",
#             "small": "tiny"}
#     dict1=input("find the word")
#     print(dict[dict1])
#
# except Exception as e:
#     print("invalid word",e)


# 9 sets
#
# s=set()
# s.add(1)
# s.add(2)
# s.add(2)
# #s1=s.union({1,2,3})
# s2=s.intersection({1,2,3})
# print(s,s2) #we can also create this in list but diff is list can take duplicate values where as set has unique values

"""
print(type(s))
l=[1,2,3,4]
s_from_list = set(l)
print(list)
"""


# 10 else if

# var1=7
# var2=100
#
# var3=int(input("enter no"))
#
# if var3>var2:
#     print("greater")
#
# elif var3==var2:
#     print("equal")
#
# else:
#     print("lesser")

#
# list=[1,2,3]
#
# if 2 in list:
#     print("yes")
#
# else:
#     print("no")
#
# if 5 not in list:
#     print("yes")
#
# else:
#     print("no")


#faulty calculator
#
# print("1st no")
# num1=int(input())
#
# print("2nd no")
# num2=int(input())
#
# print("which condition","+,-,%,/,*")
# num3=input()
#
# if num1==45 and num2==3 and num3=="*":
#     print("555")
#
# elif num1==56 and num2==9 and num3=="+":
#     print("77")
#
# elif num1==5 and num2==6 and num3=="/":
#     print("4")
#
# elif num3=="+":
#     print(num1+num2)
#
# elif num3 == "*":
#     print(num1 * num2)




# 11 loops


# fri=["veda","sam","khush"]
#
# for i in fri:
#     print(i)


# fri=[["veda",1],["sam",2],["khush",3]]
# dict1=dict(fri)
# print(dict1)
#
#
# for i,j in dict1.items():  # if you wanna fetch both key and val then u have to use .items() and if u just want keys not val then u can direct fetch it as list
#     print(f"{i} and {j}")

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

# while loop

# i=45
#
# while(i>0):
#     print(i)
#     i=i-1
#
#
i=0

# while(i<45):
#     print(i,end="")
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
        continue

