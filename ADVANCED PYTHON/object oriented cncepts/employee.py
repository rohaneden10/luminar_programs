class Employee:
    def setVal(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printVal(self):
        print("name=",self.name)
        print("age=",self.age)
        print("salary=",self.salary)
obj=Employee()
obj.setVal('babu',23,23333)
obj.printVal()