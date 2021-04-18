import re
x="a{3}"#no of position of a as group ie whe ther is a three times
r="aaaasaf asfasfaaa"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())