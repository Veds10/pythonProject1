# F strings
# import math
#

# me = "Harry"
# a1 = 3

#type1
# # a = "this is %s %s"%(me, a1)

#type2
# # a = "This is {1} {0}"
# # b = a.format(me, a1)
# # print(b)

#type3(most flexible)
# a = f"this is {me} {a1} {math.cos(65)}"
# # time
# print(a)

# count of even and odd no

lst=[12,13,14,15,156,233,78,90]
def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1

        else:
            odd+=1

    return even,odd

even,odd=count(lst)

print(f"this is even count{even},this is odd count{odd}")

