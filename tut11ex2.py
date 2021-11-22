#faulty calculator

print("1st no")
num1=int(input())

print("2nd no")
num2=int(input())

print("which condition","+,-,%,/,*")
num3=input()

if num1==45 and num2==3 and num3=="*":
    print("555")

elif num1==56 and num2==9 and num3=="+":
    print("77")

elif num1==5 and num2==6 and num3=="/":
    print("4")

elif num3=="+":
    print(num1+num2)

elif num3 == "*":
    print(num1 * num2)

elif num3 == "/":
    print(num1 / num2)

elif num3 == "-":
    print(num1 - num2)





