a=int(input("ist mark"))
b=int(input("2nd mark"))
c=int(input("3rd mark"))
d=int(input("4th mark"))
avg=0
avg=(a+b+c+d)/200
percentage=avg*100
print(percentage)
if(percentage>90):
    print("a+")
elif(80<percentage<89):
    print("a")
elif(70<percentage<79):
    print("b=")
elif(60<percentage<69):
    print("b")
elif(50<percentage<59):
    print("c+")
elif(40<percentage<49):
    print("c")
else:
    print('fail')