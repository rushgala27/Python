#This is the user program for Calculator

#First we import the 'calculator' where methods are defined
import calculator as cal

i = 1
while(i!=0):
    print("Enter 1 for addition,2 for subtraction,3 for multiplication,")
    print("4 for division,5 for raising to a power,6 for squaring a number")
    print("7 for cube of a number,8 for square root,9 for cube root,10 for increment.")
    inp = int(input())
    if(inp == 1):
        num1 = float(input("Enter number 1:"))
        num2 = float(input("Enter number 2:"))
        cal.add(num1,num2)
    if(inp == 2):
        num1 = float(input("Enter number 1:"))
        num2 = float(input("Enter number 2:"))
        cal.sub(num1,num2)
    if(inp == 3):
        num1 = float(input("Enter number 1:"))
        num2 = float(input("Enter number 2:"))
        cal.mul(num1,num2)
    if(inp == 4):
        num1 = float(input("Enter number 1:"))
        num2 = float(input("Enter number 2:"))
        cal.divide(num1,num2)
    if(inp == 5):
        num1 = float(input("Enter base:"))
        num2 = float(input("Enter power:"))
        try:
            res = cal.power(num1,num2)
            print(res)
        except (ValueError,TypeError) as e:
            print(e)
    if(inp == 6):
        num = float(input("Enter the number:"))
        cal.square(num)
    if(inp == 7):
        num = float(input("Enter the number:"))
        cal.cube(num)
    if(inp == 8):
        num = float(input("Enter the number:"))
        cal.sqroot(num)
    if(inp == 9):
        num = float(input("Enter the number:"))
        cal.curoot(num)
    if(inp == 10):
        num = float(input("Enter the number:"))
        cal.increment(num)
    i = int(input("Enter 1 to continue or 0 to exit:"))
print("Thank You!")