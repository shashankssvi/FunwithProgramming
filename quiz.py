f1=open("question.txt")
f2=open("answer.txt")
f3=open("key.txt")
fkey=f3.readline()
fkey=fkey.split(",")
list1=f1.readlines()
total=0
all1=["a","b","c","d"]
lista=[]
lista1=[]
def all(i):
    lista1.append(i+1)
    lista1.append(list1[i])
    
for i in range(0,len(list1),1):
    list2=f2.readline()
    print((i+1),".",list1[i].replace("\n",""))
    print()
    t=0
    while t<4:
        list3=list2.split("}{")
        print(all1[t]+")",list3[t].replace("\n",""))
        
        t+=1
    print()
    a=input("option: ")
    print()
    
    if a!=fkey[i]:
        if fkey[i]=="a":
            all(i)
            lista.append("a")
            lista.append(list3[0])   
        elif fkey[i]=="b":
            all(i)
            lista.append("b")
            lista.append(list3[1])
        elif fkey[i]=="c":
            all(i)
            lista.append("c")
            lista.append(list3[1])
        elif fkey[i]=="d":
            all(i)
            lista.append("d")
            lista.append(list3[3])
    else:
        total+=1
print("______________________end_______________________")
print("\nTotal score is ",total," out off",len(list1),"\n")

k=len(lista)

for i in range(0,int(k/2),1):
    print(lista1[2*i],".",lista1[2*i+1].replace('\n',''))
    print(lista[2*i]+")",lista[2*i+1],"\n")
    
