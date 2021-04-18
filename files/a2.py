list=[]
f=open("messi","r")
sum=0
for lines in f:
    list.append(int(lines.rstrip("\n")))#intilay read as astring and we convert it to integer
for i in list:
    sum+=i
print(list)
print(sum)
#rstrip is used to remove end characters
#lstrip used to remove first character