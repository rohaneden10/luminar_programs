class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print_emp(self):
        print(self.name)
employees=[]
f=open("employees")
for lines in f:
    eid,name,desig,sal=lines.rstrip("\n").split(",")
    e1=Employee(eid,name,desig,sal)
    e1=employees.append(e1)
#e1=Employee(1000,"varun","developer",21333)
#e2=Employee(1001, "manu", "developer", 23433)
#e3=Employee(1002, "joby", "qa", 23533)
#e4 = Employee(1003, "sabu", "marketing", 21432)
#employees.append(e1)
#employees.append(e2)
#employees.append(e3)
#employees.append(e4)
#sal=[]
#for emp in employees:
#    sal.append(emp.salary)
#print(sal)
#print(employees)
salary=max(list(map(lambda emp:emp.salary,employees)))
print(salary)