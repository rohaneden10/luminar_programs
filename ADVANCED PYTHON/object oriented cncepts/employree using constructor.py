class Employee:
    company_name="lumniar"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printVal(self):
        print("name=",self.name)
        print("age=",self.age)
        print("salary=",self.salary)
        print("company name ",Employee.company_name)
emp=Employee('babu',23,2324234322323324324234234234235)
emp.printVal()