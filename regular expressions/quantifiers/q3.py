import re
x="a?"#count a as each incluing no f a ie gets where the pattern occurs not as group but individually unline a+
r="afsafsfsdgdsvcv"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())