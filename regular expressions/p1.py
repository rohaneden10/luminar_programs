#regular expressions used for pattern matching
#for ths we use 're' module
#used for validations
import re
count=0
matcher=re.finditer('ab','abababab')#finditeris used for iteration#pattern to search and patter search string
for i in matcher:
    count+=1
print(count)