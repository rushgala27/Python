#This is the file where methods are defined for the calculator

import math as m

def add(a,b):
    print(a + b)
def sub(a,b):
    print(a - b)
def mul(a,b):
    print(a*b)
def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Divisor cannot be 0")
def power(a,b):
    if a == 0 and b<=0:
        raise ValueError('0 cannot be raised to negative number or 0')
    if a<0 and not type(b) is int:
        raise TypeError('Only integral powers allowed for negative numbers')
    return m.pow(a,b)
def square(a):
    print(a*a)
def cube(a):
    print(a*a*a)
def sqroot(a):
    try:
        print(m.sqrt(a))
    except:
        print("Number entered cannot be negative")
def curoot(a):
    if a>=0:
        print(a**(1/3))
    else:
        c = abs(a)
        print(-(c**(1/3)))
def increment(a):
    a = a + 1
    print(a)