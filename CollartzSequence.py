#Write a program to implement collartz sequence
def collartz(num):
    if(num == 4):
        print(2)
        print(1)
        return
    else:
        if(num%2 == 0):
            num = num//2
        else:
            num = num*3 + 1
        print(num)
        collartz(num)

num = int(input("Enter any positive integer : "))  
print(num)
collartz(num)