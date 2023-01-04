#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random as r
n = r.randint(0,10)
guess = int(input("Enter the number: "))
while(guess!=n):
    if guess>n:
        print("Too high!Try again")
    else:
        print("Too low!Try again")
    guess = int(input("Enter the number: "))
print("You have guessed correct")