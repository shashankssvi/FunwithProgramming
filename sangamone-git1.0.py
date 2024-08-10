import os
print("this shows .git folder in this directory and all ints sub directories")
for i,j,k in os.walk(os.getcwd()):
    for l in j:
        if l==".git":
            print(os.path.join(i,l))