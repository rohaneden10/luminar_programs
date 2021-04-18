f=open("filem","r")
#n=0
#for lines in f:
   # n+=1
#    print(lines)
#    words = lines.rstrip("\n").split(",")
  #  print(words)
class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
        print(self.name)
        print(self.age)
    def __str__(self):
        return self.name
for lines in f:
    words =lines.rstrip("\n").split(",")
    obj=Person(words[0],words[1])
    print(obj)






