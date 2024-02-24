num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))
if (num1>num2) and (num1>num3):
    print("num1 is the largest number")
elif (num2>num1) and (num2>num3):
    print("num2 is largest number")
elif (num3>num1) and (num3>num2):
    print("num3 is larest number ")
else:
    print("all number are equal")
