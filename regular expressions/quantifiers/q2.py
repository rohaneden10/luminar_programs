import re
x="a*"#count including where a and where theree is no a ie considers all position and prints all postioons

r="asfdsfsdfdsfds"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())