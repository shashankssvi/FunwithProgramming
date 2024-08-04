def ami(b):
    a=0
    for i in range(1,b):
        if b % i==0:
            a+=i
    return a
b=int(input("Enter the first number: "))
for i in range(1,b):
    for j in range(1,i):
        if i==ami(j) and j==ami(i) and i!=j:
            print(i,j)
