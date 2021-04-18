lst=["10","20","babu","sugu","10.3","10"]
n=input("enter a element")
flag=0
for i in lst:
    if(n==i):
        print(i,"found")
        flag=1
if(flag==0):
   print("not found")
#linear search
#inceased complexity
#binary search reduces complexity