import re
x="a{1,3}"#when min no of a is 1 and max no of a is 3
r="aaaasaf asfasfaaa"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())