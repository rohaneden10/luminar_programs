lst=[1,2,3,4,5,6,7,8]
n=int(input())
for i in lst:
    for j in lst:
        if((i+j)==n):
            print("(",i,j,")")

