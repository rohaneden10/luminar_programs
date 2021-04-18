pattern="ABDBA"
dic={}
for i in pattern:
    if((i in dic)==False):
        dic[i]=1
    else:
        print(i)
        break
print(dic)