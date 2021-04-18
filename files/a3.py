even=[]
odd=[]
list=[]
f=open("C:/Users/hp/PycharmProjects/pamb1/files/messi","r")
for i in f:
    list.append(int(i.rstrip("\n")))
    if((int(i.rstrip("\n")))%2==0):
        even.append(int(i.rstrip("\n")))
    else:
        odd.append(int(i.rstrip("\n")))

print(list)
print(even)
print(odd)