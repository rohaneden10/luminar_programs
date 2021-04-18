class College:
    collegename="LT"
    def __init__(self,name,roll):
        self.roll=roll
        self.name=name
    def printVal(self):
        print("collegename=",self.collegename)
        print("name of student",self.name)
        print("rollmo",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
ob=College("anu",21)
print(ob)