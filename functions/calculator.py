def calculator():
    print("1:add")
    print("2:sub")
    print("3:mul")
    print("4:div")
    a=int(input("enter 1st no"))
    b=int(input("enter 2nd no"))
    c=int(input("enter the choice"))
    if(c==1):
        print("addition",a+b)
    elif(c==2):
        print("difference",a-b)
    elif(c==3):
        print("product",a*b)
    elif(c==4):
        print("divison",a/b)
    else:
        print("ivalid option")
calculator()

