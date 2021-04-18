
try:
    i=int(input("enter a no"))#try block has the main code
    print(i)
except:
    print("enter a integer")

finally:
    print("inside finally")#finally block works always
