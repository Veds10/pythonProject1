# i=1
# while i<=7:
#     print("tele",end=" ")
#     j=1
#     while j<=6:
#         print("scope", end=" ")
#         j=j+1
#     i=i+1
#     print()
"""
i=0
while i<=6:
    print("*",end="")
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    i+=1
    print()
"""
# i=7
# while i>1:
#     print("*",end="")
#     j=7
#     while j>=i:
#         print("*",end="")
#         j=j-1
#     i=i-1
#     print()

# for hash pattern while and for
# i=0
# while i<=3:
#     print("#",end=" ")
#     j=0
#     while j<=2:
#         print("#",end=" ")
#         j=j+1
#     i=i+1
#     print()
#
# for i in range(4):
#     for j in range(4-i):
#         print("#",end=" ")
#     print()
#
# for i in range(4):
#     for j in range(4):
#         print("#",end=" ")
#     print()

for i in range(-4):
    for j in range(-4+i):
        print("#",end=" ")
    print()