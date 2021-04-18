cd=int(input("enter current date"))
cm=int(input("enter current month"))
cy=int(input("enter current year"))
bd=int(input("enter nirth date"))
bm=int(input("enter birth month"))
by=int(input("enter birthyear"))
if(cm>=bm):
    print(cy-by,"years old")
elif(cm<bm):
    cy=cy-1
    print(cy-by,"years old")
elif(cm==bm):
    if(cd<bd):
        cy = cy - 1
        print(cy-by,"years old")
    else:
        print((cu-by)-1),"ys old"

