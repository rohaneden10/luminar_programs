import re
x="[A-Z]"#CHECK FOR ATO Z
matcher=re.finditer(x,"affidjsdijoli")
for match in matcher:
    print(match.start())
    print(match.group())
x="\s"#check for space
x="\d"#checkfor digits
x="\D"#except digits
x="\w" #check for words except special characters
x="\W"#FOR special characters