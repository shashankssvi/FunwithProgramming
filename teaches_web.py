#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
f1=open("TeacherWebsite.txt","r")
info1=f1.readlines()
len1=len(info1)
masterlist=[]
subjects=[]

for i in range(0,len1,1):
    list1=info1[i].split(":")
    subject="1"+list1[0]
    list2=list1[1].replace("\n","").split(",")
    masterlist.append(list2)
    subjects.append(subject)
    os.mkdir(subject)

for j in range(0,len1,1):
    len2=len(masterlist[j])
    for i in range(0,len2,1):
        dir1=subjects[j]+"/"+masterlist[j][i]
        os.mkdir(dir1)


# In[ ]:




