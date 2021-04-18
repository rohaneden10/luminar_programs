lst=[[1,"babu",17000],[2,"bsin",56666],[3,"lsafs",2432435]]
sum=0
for i in lst:
    print(i)
for i in lst:
    if(i[2]>17000):
        print(i[1])
for i in lst:
    sum+=i[2]
print(sum)
