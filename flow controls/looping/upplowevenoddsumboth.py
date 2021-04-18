u=int(input("upp lmit"))
l=int(input("lower limit"))
odd=0
even=0
for i in range(l,(u+1)):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i
print("sum of ecen nos",even)
print("odd nos sum",odd)
