# using of array can be done using following ways
#
# import array
# # or
# import array as arr
# # or

from array import *   # way more convinient
# vals= array("i",[1,2,3])
# for i in vals:
#     print(i)
#
# print("* * * * *")
#
# vals1= array("u",["a","e","i"])
# for i in vals1:
#     print(i)

# sqrt of no
# newarr= array(vals.typecode, (a*a for a in vals) )
# for e in newarr:
#     print(e)
#

# creating array taking values from user

# arr= array("i",[])
#
# n=int(input("how many no to enter"))
# for i in range(n):
#     x=int(input("enter the next value"))
#     arr.append(x)
#
# print(arr)
#
# k=int(input("enter the val to be search"))
# print(arr.index(k))     # gives the index no

# creating types of array using numpy which is more easy then above

from numpy import *
arr= array([1,2,3,4,5],int)
arr= array([1,2,3,4,5],float)
print(arr.dtype)
print(arr)

# adding to arrays

a1=array([1,2,3,4])
a2=array([1,2,3,4])
a3=a1+a2
print(a3)


