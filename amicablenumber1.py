def ami(b):
    a=0
    for i in range(1,b):
        if b % i==0:
            a+=i
    return a
b=int(input("Enter the first number: "))
d=int(input("Enter the secont number: "))
a=ami(b)
c=ami(d)
if b==c and d==a and b!=d:
    print(b,"and",a,"are the ambicable numbers")
