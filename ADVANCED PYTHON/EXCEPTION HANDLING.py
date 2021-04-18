#a=int(input("n1"))
b=int(input("n2"))
#exception handling is used to clear enexpected errors
#two blocks try and exception
try:
    res=a/b
    print("res",res)
except:
    print("exceptin iccured")
#exception block work if exception occur