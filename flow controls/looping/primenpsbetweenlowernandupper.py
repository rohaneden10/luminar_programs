u=int(input("upp lmit"))
l=int(input("lower limit"))
flag=0
for n in range(l,u+1):
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
        else:
            flag=0
    if (flag == 0):
        print(n)
    flag=1

