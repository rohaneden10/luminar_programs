f=open("assignm","r")
loc={}
prof={}
age={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    print(words)
    if((words[-1]) not in loc):
        loc[(words[-1])]=1
    else:
        loc[(words[-1])]+=1
    if ((words[3]) not in age):
        age[(words[3])] = 1
    else:
        age[(words[3])] += 1
    if ((words[4]) not in prof):
        prof[(words[4])] = 1
    else:
        prof[(words[4])] += 1

print(prof)
print(loc)
print(age)