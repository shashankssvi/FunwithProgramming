#!/usr/bin/env python
# coding: utf-8

# In[86]:


survived=[]
names=[]
sex=[]
age=[]
male=[]
female=[]
others=[]
children=[]
dc=[]
sc=[]
f1=open("titanic.csv","r")
f1.readline()
list1=f1.readlines()
len1=len(list1)
for i in range(0,len1,1):
    
    info1=list1[i]
    list2=info1.split(",")
    survived.append(int(list2[1]))
    names.append(list2[4])
    sex.append(list2[5])
    if list2[6] == "":
        age.append(40)
    else:
        age.append(int(float(list2[6])))

total_survived=sum(survived)
total_deceased=len1-total_survived
for i in range(0,len1,1):
    if sex[i]=="male":
        male.append(names[i])
    elif sex[i]=="female":
        female.append(names[i])
    else:
        others.append(names[i])
        
for i in range(0,len1,1):
    if age[i] < 10:
        children.append(names[i])
        if age[i] < 10 and survived[i] == 1:
            dc.append(names[i])
        if age[i] < 10 and survived[i] == 0:
            sc.append(names[i])

total_male=len(male)
total_female=len(female)
total_others=len(others)
total_children=len(children)
total_dc=len(dc)
total_sc=len(sc)
print("total number of people in titanic",len1,"in that-")
print("number of people survived",total_survived)
print("number of people deceased",total_deceased)
print("number of males",total_male)
print("number of females",total_female)
print("number of others",total_others)
print("number of children",total_children)
print("number of children survived",total_sc)
print("number of children deceased",total_dc)


# In[ ]:




