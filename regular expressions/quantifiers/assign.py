import re
n=input("enter a no")
x='[+][9][1]\d{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
