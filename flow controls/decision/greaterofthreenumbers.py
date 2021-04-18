a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd number"))
if(a>b)&(a>c):
    print("a is greater",a)
elif(b>a)&(b>c):
    print("b is greater",b)
elif(c>a)&(c>b):
    print("c is greater")
else:
    print("all are qqual")