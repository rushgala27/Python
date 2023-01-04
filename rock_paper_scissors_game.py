#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random as r
option_list = ["rock","paper","scissors"]

player2 = r.choice(option_list)
while(True):
    player1 = input("Select rock,paper or scissors: ")
    if player1 not in option_list:
        print("Wrong option selected!Try again.")
    else:
        break
print("Player 2 selected:",player2)
if player1=="rock" and player2=="paper":
    print("Player 2 won!")
elif player1=="paper" and player2=="scissors":
    print("Player 2 won!")
elif player1=="scissors" and player2=="rock":
    print("Player 2 won!")
elif player1==player2:
    print("Tie")
else:
    print("Player 1 won!")

