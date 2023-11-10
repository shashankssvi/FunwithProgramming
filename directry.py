#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
x=input("file name with .txt ")                       #textfile name contines the directry detiles
x=str(x)
f1=open(x,"r")  
teacher=[]
subject=[]
list1=[]
info=f1.readlines()
list1=info
len1=len(list1)
def mod_web():                                         #import module (it gives the instruction)
    for j in range(0,len1,1):
        subject=list1[j].split(":")
        sub=subject[0]
        teacher=subject[1].replace("\n","").split(",")
        len2=len(teacher)

        for i in range(0,len2,1):
            t1=teacher[i]
            s=os.makedirs(os.path.join(sub, t1))
            
y=input("enter 1 to create directory")                  #function copy without seeing the module
y=int(y)
if y == 1:
    mod_web()
    print("successfully created the directory")
else:
    print("unsuccessfull")


# In[ ]:




