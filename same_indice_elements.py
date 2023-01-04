#!/usr/bin/env python
# coding: utf-8

# In[2]:


input_list = [[10,20,3,24],[655,334,13,56],[35,678,9,8]]
output_list = []

for i in range(len(input_list[0])):
    temp = []
    for j in range(len(input_list)):
        temp.append(input_list[j][i])
    output_list.append(temp)
    
print(output_list)

