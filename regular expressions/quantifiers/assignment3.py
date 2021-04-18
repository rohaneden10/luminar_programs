import re
n=input("enter a no")
x='[a-zA-Z]+[0-9]+$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
