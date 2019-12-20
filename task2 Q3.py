#!/usr/bin/env python
# coding: utf-8

# In[4]:


for i in range(1999,3201):
    if(i%7==0 and i%5!=0):
        print(i,end=",")


# In[5]:


x=input("Enter your first name : ")
y=input("Enter your last name : ")
print(y+" "+x)


# In[6]:


pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# In[8]:


val= input("Input some comma seprated numbers : ")
list = val.split(",")
print('List : ',list)


# In[12]:


n=4;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[13]:


x=input('Enter a word: ')
x=x[::-1]
print(x)


# In[ ]:




