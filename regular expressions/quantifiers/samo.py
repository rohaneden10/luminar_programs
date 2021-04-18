import re
n="hellooo"
x='\w{6}'
match=re.fullmatch(x,n)#checkinng if word is sixletter
if match is not None:
    print("valid")
else:
    print("invalid")
