import re
x="[^abc]"#except abc
matcher=re.finditer(x,"afsdbsdufisdikasjdhkasjdh")
for match in matcher:
    print(match.start())
    print(match.group())