def cube():
   a=int(input("number="))
   cube=a*a*a
   print(cube)
cube()

#def cube(a):
 #  a=int(input("number="))
  # cube=a*a*a
   #print(cube)
#cube(3)

def cubeN(a):
   a=int(input("number="))
   cube=a*a*a
   return cube
data=cubeN(3)
print(data)
