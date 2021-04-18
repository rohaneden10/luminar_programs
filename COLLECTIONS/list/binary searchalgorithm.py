lst=[1,2,3,4,5,7,8,6,9]
lst.sort()
print(lst)
n=int(input("enter a element"))
low=0
flag=0
upper=len(lst)-1
while(low<=upper):
    mid=(low+upper)//2
    print(lst[low:upper])

    if(n>lst[mid]):
        low=mid+1
    elif(n<lst[mid]):
        upper=mid-1
    elif(n==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element foudn")
else:
    print("elelmet not found")

