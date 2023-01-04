#Program to find if a given number is Smith number or not

#Find sum of digits of the number
def Sum_digits(num):
    sum = 0
    while(num%10!=0):
        sum+=num%10
        num = num//10
    return sum
    
#Check if the number is a prime number
def Prime(num):
    for i in range(2,num):
        if((num%i)==0):
            return False
        else:
            continue
    return True

#Find prime factors of the number
fact = []
def Sum_primefactors(num):
    temp = num
    for j in range(1,temp):
        for i in range(2,temp+1):
            if((temp%i)==0 and Prime(i)):
                fact.append(i)
                temp = temp//i
    sum = 0
    for i in fact:
        m = 0
        if(i>9):
            m = Sum_digits(i)
            sum+=m 
        else:
            sum+=i
    return sum

#Find Smith number    
def Smith_number(num):
    if(num==1):
        print("The number 1 does not lie in definition of Smith number")
    elif(Prime(num)==True):
        print("The number is prime number so it does not lie in definition of Smith number")
    elif(Sum_digits(num)==Sum_primefactors(num)):
        print("The number is a Smith number")
    else:
        print("The number is not a Smith number")

n = int(input("Enter a positive integer : "))
Smith_number(n)

