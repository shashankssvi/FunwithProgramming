lis=open("cert.txt","r")
war=lis.readline().split(" ")
for i in range(0,5,1):
    str(war1[i])
print("the output of ",war,"is")

r2=war[0],war[1],war[2],war[3],war[4]
print(r2)

temp1=war[1]
war[1]=str(war[4])
war[4]=temp1

a=int(war[0])/int(war[3])

r1= "1",war[1],war[2],str(a),war[4]
print(r1)


print()

war1=lis.readline().split(" ")
print("the output of ",war1,"is")
for i in range(0,5,1):
    str(war1[i])

r3= war1[0],war1[1],war1[2],war1[3],war1[4]
print(r3)

temp=war1[1]
war1[1]=str(war1[4])
war1[4]=temp

b=int(war1[0])/int(war[3])

r4="1",war1[1],war1[2],str(b),war1[4]
print(r4)
f1=open("out.txt","w")
f1.write(str(r3))
f1.write("\n")
f1.write(str(r4))
f1.write("\n")
f1.close()
f2=open("out.txt","a")
f2.write(str(r2))
f2.write("\n")
f2.write(str(r1))
f2.write("\n")
f2.close()
