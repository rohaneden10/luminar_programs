import re
x="[abc]"#measn eitheraorb or c
matcher=re.finditer(x,"abasfowr#@$")
for match in matcher:
    print(match.start())
    print(match.group())
