a=int(input("enter no of classes held"))
b=int(input("enter no of classes attended"))
print("percentage of classes attended is",(b/a)*100)
if(((b/a)*100)<75):
    print("not eligibele")
else:
    print("eligile")