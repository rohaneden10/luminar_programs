lst=[]
evenlst=[]
odd=[]
for i in range(50,201):
    lst.append(i)
    if(i%2==0):
        evenlst.append(i)
    else:
        odd.append(i)
print(lst)
print(evenlst)
print(odd)