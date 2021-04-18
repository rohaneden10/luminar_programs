import re
x="a$"#check if string wnding with a
r="aaaasaf asfasfaaa"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())