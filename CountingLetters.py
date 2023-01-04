#Counting full stops, words, letters, unique words, words starting with vowel in a paragraph

f = open('lion.txt','r') 
b = 0
for i in f:
    a = i.split('.')
    try:
        a.remove('\n')
    except:
        pass
    b = b + len(a)
print("The number of full stops are ",b)
f.close()

f = open('lion.txt','r') 
count = 0
for i in f:
    a = i.split(' ')
    for j in range(len(a)):
        if(a[j]=='(' or a[j]=='.' or a[j]==')' or a[j]==',' or a[j]=='!' or a[j]=='?' or a[j]=='/' or a[j]==';' or a[j]==':'):
            pass
        else:
            count = count + 1
print("The number of words are ",count)          
f.close()

f = open('lion.txt','r')
a = 0
for i in f:
    b = i.split(' ')
    for j in range(0,len(b)):
        a = a+len(b[j])
print("The number of letters are ",a)
f.close()

f = open('lion.txt','r') 
a = []
for i in f:
    b = i.split(' ')
    a = list(set(b))
    counter = 0
    for j in range(len(a)):
        if(a[j]=='(' or a[j]=='.' or a[j]==')' or a[j]==',' or a[j]=='!' or a[j]=='?' or a[j]=='/' or a[j]==';' or a[j]==':'):
            counter = counter+1
print("The number of unique words are ",len(a)-counter)
f.close()

f = open('lion.txt','r')
count = 0
for i in f:
    a = i.split(' ')
    b = ['a','e','i','o','u','A','E','I','O','U']
    for j in range(len(a)):
        if(a[j].startswith(tuple(b))):
            count = count+1
print("The number of words starting with vowel are ",count)
f.close()