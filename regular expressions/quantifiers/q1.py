import re
x="a+"#a includinggroup
r="aaaaaaefdfa sfsa afdsf"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())