
"""
print("enter 1st no")
num1=int(input())
print("enter 2nd no")
num2=int(input())

print("sum is",num1+num2)
"""

# with try catch

try:
    print("enter 1st no")
    num1 = int(input())
    print("enter 2nd no")
    num2 = int(input())

    print("sum is", num1 + num2)

except Exception as e:
    print(e)
print("end")



