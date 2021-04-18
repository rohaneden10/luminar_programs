class Person:
    def __init__(self,name,roll,branch,mark):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.mark=mark
    def printVal(self):
            print(self.name)
            print(self.roll)
            print(self.branch)
            print(self.mark)
f=open("work","r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    print(words)
    obj=Person(words[0],words[1],words[2],words[3])
    mark=int(words[3])
    if(mark>190):
        obj.printVal()
