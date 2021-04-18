f=open("task","r")
#for i in f:
   # print(i)
dic={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    print(words)
    for i in words:
        if(i not in dic):
            dic[i] = 1
        else:
            dic[i]+= 1
print(dic)

