class Employee:
    companyname="LT"
    def empdet(self,name,age,id,salary):
        self.age=age
        self.name=name
        self.id=id
        self.salary=salary
    def printVal(self):
        print(self.age)
        print(self.name)
        print(self.id)
        print(self.salary)
    def __str__(self):
        return str(self.id)#since id is integer we are using str and if its stringno str needed
emp=Employee()
emp.empdet("babu",21,2,345543)
print(emp)