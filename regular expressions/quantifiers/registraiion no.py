import re
f=open("asmo","r")
x='\w{2}\d{2}\w{2}\d{4}'#or[kK][Ll]\d{2}[a-zA-Z]{2}\D{4}$
lst=[]
for lines in f:
    words=lines.rstrip("\n")
   # print(words)
    match = re.fullmatch(x,words)
    if match!=None:
        lst.append(words)
        #print(lst)
print(lst)
