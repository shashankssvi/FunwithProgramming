f1=open("Pincode_30052019.csv","r")
info1=f1.readlines()
location1=[]
pincode1=[]
district1=[]
state1=[]
for i in info1:
    list1=i.replace("\n","").split(",")
    location1.append(list1[3])
    pincode1.append(list1[4])
    district1.append(list1[7])
    state1.append(list1[8])

pincode="576227"
len1=len(pincode1)
for i in range(0,len1,1):
    if pincode1[i]==pincode:
        s1=pincode1[i]+","+location1[i]+","+district1[i]+","+state1[i]
        print(s1)

