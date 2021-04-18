import re
count=0
matcher=re.finditer('ab','abababab')#finditeris used for iteration#pattern to search and patter search string
for match in matcher:
    print("match available at",match.start())#returns positions
    print("group=",match.group())#which object findmatch
    count+=1
print(count)