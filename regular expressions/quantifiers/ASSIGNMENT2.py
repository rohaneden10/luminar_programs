import re
f=open("register no lum","r")
x="([L][U][M]\d{2}[P][Y]\d{3})"
lst=[]
g= open("mes","a")#file created in append mode ie file crreatd and write unlike w mode which overwrites th exsiting data
for lines in f:
    words=lines.rstrip("\n")
    print(words)
    match = re.fullmatch(x,words)
    if match!=None:
        lst.append(words)
        g.write(words)
        g.write("\n")
    #print(lst)
print(lst)
1