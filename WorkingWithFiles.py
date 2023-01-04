# path = "C:\\Users\\rusha\\old laptop\\python\\" + "r.txt"
# with open(path,'a') as f:    #a stands for append mode
#     f.write('\n4 Fourth Line')

# f = open(path,'r')
# cont = f.read()
# print(cont)

path = "C:\\Users\\rusha\\old laptop\\python\\" + "r.txt"     #Write the file path which you want
with open(path,'w') as f:    #w stands for write mode
    f.write('\n4 Fourth Line')

f = open(path,'r')    #r stands for read mode
cont = f.read()
print(cont)
f.close()