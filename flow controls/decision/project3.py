a=str(input("enter sex"))
b=str(input("enter marital status"))
c=int(input("enter age"))
if(a=="F"):
    print("URBAN AREA")
elif(a=="M")&(20<c<30):
    print("anywhere")
elif(a=="M")&(40<c<60):
    print("URBAN AREAS")
else:
    print("error")
