import re
n=input("enter a no")
x='^a[a-zA-Z0-9\W]*b$'#* MEANS INCLUDING ALL COBINATIONS OF A
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
