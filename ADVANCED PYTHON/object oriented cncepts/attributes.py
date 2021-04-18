class Person:#first letter is capital useful
    def setVal(self,name,age):#the attributes passed are the attributes in class ie why we use
        self.age=age
        self.name=name
    #self is a keyword for oop #while in class #if methood outside class no self is needed
    def printVal(self):
        print("name=",self.name)
        print("age",self.age)
obj=Person()
obj.setVal('ram',23)
obj.printVal()
