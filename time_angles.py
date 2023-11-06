for j in range(1,13,1):
    print(str(j)+":00 -  \b0"+" \b°")
    print(str(j)+":05 -  \b30"+" \b°")
    for i in range(2,12,1):
        s=i*30
        print(str(j)+":"+str(5*i)+" -  \b"+str(s)+" \b°")
    print()
