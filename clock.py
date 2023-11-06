h=int(input())
a=0+h*15
if h<=24 and h>0:
    if h<12:
        print("at",h,"oclock AM or PM the houres hand at ",a,"digree if we concider 12 or 24 as 0 degree\n")
        for i in range(0,12,1):
            s=0+i*30
            print(h,":",5*i,"is",s)
        print(h+1,": 00","is",360)
    elif h<=24 and h>=12:
        print("at",h,"oclock PM the houres hand at ",a,"digree if we concider 24 as 0 degree\n")
        for i in range(0,12,1):
            s=0+i*30
            print(h,":",5*i,"is",s)
        print(h+1,": 00","is",360)
else:
    print("input between 1 to 24 only")
