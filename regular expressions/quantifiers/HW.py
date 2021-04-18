import re
n=input("enter a no")
x="\D{8,15}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
