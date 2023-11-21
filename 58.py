import math as m
for j in range(3,100,1):
    for i in range(j,100,1):
        s1=float(m.sqrt(j*j+(i+1)*(i+1)))
        s2=int(s1)
        if s1-s2==0:
            print("(",j,",",i+1,",",s2,") is a triad")
