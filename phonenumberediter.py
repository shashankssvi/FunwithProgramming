def parsephonenumbers(infile,outfile,cc):
    f1=open(infile,"r")
    f2=open(outfile,"w")
    list1=["IN","US"]
    list2=["91","1"]
    pos=list1.index(cc)
    cc1=list2[pos]
    cc2="+"+cc1
    for i in range(0,8,1):
        s1=f1.readline().replace("\n","").replace(" ","").replace("-","").replace(",","")
        len1=len(s1)
        s2=""
        if len1==13 and s1[0:3]==cc2:
            s2=s1
        if len1==12 and s1[0:2]==cc1:
            s2="+"+s1
        if len1==11 and s1[0]=="0":
            s2=s1.replace(s1[0],cc2)
        if len1==10:
            s2=cc2+s1
        print(s2)
        f2.write(s2)
        f2.write("\n")
    f2.close()

parsephonenumbers("phone1.txt","phone2.txt","IN")
