class Employee:
    company_name="lumniar"
    def setVal(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printVal(self):
        print("name=",self.name)
        print("age=",self.age)
        print("salary=",self.salary)
        print("company name ",Employee.company_name)
emp=Employee()
emp.setVal('babu',23,23333)
emp.printVal()