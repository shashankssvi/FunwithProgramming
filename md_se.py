#!/usr/bin/env python
# coding: utf-8

# In[10]:


survived=[]
names=[]
sex=[]
age=[]
male=[]
female=[]
others=[]
children=[]
deceased_child=[]
survived_child=[]
f1=open("titanic.csv","r")   #ignore headers in first line
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
        age.append(40)      #if age is absent, assume that age of person=40. It can be anything
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
            deceased_child.append(names[i])
        if age[i] < 10 and survived[i] == 0:
            survived_child.append(names[i])

total_male=len(male)
total_female=len(female)
total_others=len(others)
total_children=len(children)
total_deceased_child=len(deceased_child)
total_survived_child=len(survived_child)

#statment putting into the variable

info= "total number of people in titanic"+" "+str(len1)+" "+"in that-"
e=info
info1="number of people survived"+" "+str(total_survived)
e1=info1
info2="number of people deceased"+" "+str(total_deceased)
e2=info2
info3="number of males"+" "+str(total_male)
e3=info3
info4="number of females"+" "+str(total_female)
e4=info4
info5="number of others"+" "+str(total_others)
e5=info5
info6="number of children"+" "+str(total_children)
e6=info6
info7="number of children survived"+" "+str(total_deceased_child)
e7=info7
info8="number of children deceased"+" "+str(total_survived_child)
e8=info8
out=str(e)+"\n"+str(e2)+"\n"+str(e1)+"\n"+str(e3)+"\n"+str(e4)+"\n"+str(e5)+"\n"+str(e6)+"\n"+str(e7)+"\n"+str(e8)
print(out)


# In[ ]:




