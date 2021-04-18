lst1=[1,2,3,4,5]
lst2=[9,1,2,3,4]
lst=[]
for i in lst1:
    for j in lst2:
        if(i==j):
            lst.append(j)
print(lst)