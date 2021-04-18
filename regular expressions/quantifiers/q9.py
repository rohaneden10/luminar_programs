import re
x="^a"#chect if string as a whole starting with a
r="aaaasaf asfasfaaa"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())